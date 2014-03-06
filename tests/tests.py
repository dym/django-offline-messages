from django.contrib.auth.models import User
from django.contrib.messages import constants
try:
    from django.contrib.messages.tests import test_session as session_tests
except ImportError:
    from django.contrib.messages.tests import session as session_tests

from offline_messages.models import OfflineMessage
from offline_messages.storage import OfflineStorageEngine
from offline_messages.utils import create_offline_message


class OfflineMessagesTests(session_tests.SessionTest):
    storage_class = OfflineStorageEngine
    test_message = 'This is a test message'
    test_level = constants.DEBUG

    def create_user(self):
        return User.objects.create(username='test-user')

    def get_request(self, user=None):
        request = super(OfflineMessagesTests, self).get_request()
        if user:
            request.user = user
        return request

    def create_offline_message(self, user, message=None, level=None):
        if not message:
            message = self.test_message

        if not level:
            level = self.test_level

        create_offline_message(user, message, level)

    def assert_offline_message(self, user, message=None, level=None):
        if not message:
            expected_message =self.test_message

        if not level:
            expected_level = self.test_level

        offline_message = OfflineMessage.objects.get()
        self.assertEqual(offline_message.message, expected_message)
        self.assertEqual(offline_message.level, expected_level)

        storage = OfflineStorageEngine(self.get_request(user))
        all_messages = list(storage)
        self.assertEqual(len(all_messages), 1)
        self.assertEqual(offline_message, all_messages[0])

    def test_create_offline_storage(self):
        user = self.create_user()
        self.create_offline_message(user)
        self.assert_offline_message(user)

    def test_create_offline_storage_with_username(self):
        user = self.create_user()
        self.create_offline_message(user.username)
        self.assert_offline_message(user)

    def test_offline_message_with_session_messages(self):
        user = self.create_user()
        self.create_offline_message(user)
        # Grab the message before it is delted
        offline_message = OfflineMessage.objects.get()

        storage = OfflineStorageEngine(self.get_request(user))

        test_messages = ['one', 'two']
        session_tests.set_session_data(storage, test_messages)

        all_messages = list(storage)
        self.assertEqual(len(all_messages), 3)
        test_messages.insert(0, offline_message)
        self.assertEqual(all_messages, test_messages)

    def test_offline_message_tags(self):
        user = self.create_user()
        self.create_offline_message(user)
        offline_message = OfflineMessage.objects.get()
        expected_tags = constants.DEFAULT_TAGS.get(self.test_level)
        self.assertEqual(offline_message.tags, expected_tags)
