# -*- coding: utf-8; mode: python; -*-
from django.contrib.messages.storage.session import SessionStorage

from offline_messages.utils import create_offline_message
from offline_messages.models import OfflineMessage


class OfflineStorageEngine(SessionStorage):
    """
    Stores messages in the database (offline_messages.OfflineMessage).
    """
    
    def _get(self, *args, **kwargs):
        """ 
        Get unread offline and all online messages (which are inherently 'unread').
        """
        messages = []

        if hasattr(self.request, 'user') and self.request.user.is_authenticated():
            offline_messages = OfflineMessage.objects.filter(user=self.request.user, read=False)

            if offline_messages:
                messages.extend(offline_messages)
                offline_messages.update(read=True)

        online_messages, all_retrieved = super(OfflineStorageEngine, self)._get(*args, **kwargs)
        if online_messages:
            messages.extend(online_messages)

        return messages, True

    def _store(self, messages, *args, **kwargs):
        """ 
        Store messages. If logged in, store them offline, else, store in session.
        """
        if hasattr(self.request, 'user') and self.request.user.is_authenticated():
            for msg in messages:
                # just the basics, if you need the extra meta data, do this manually
                # and add the extra kwargs
                create_offline_message(self.request.user, msg.message, msg.level)
        else:
            messages = [msg for msg in messages if not isinstance(msg, OfflineMessage)]
            return super(OfflineStorageEngine, self)._store(messages, *args, **kwargs)
