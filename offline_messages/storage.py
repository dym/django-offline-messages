# -*- coding: utf-8; mode: python; -*-
from django.contrib.messages.storage.session import SessionStorage

from offline_messages.models import OfflineMessage


class OfflineStorageEngine(SessionStorage):
    """
    Stores messages in the database (offline_messages.OfflineMessage).
    """
    
    def _get(self, *args, **kwargs):
        """ Get offline and online messages. """
        messages = []

        if hasattr(self.request, "user") and self.request.user.is_authenticated():
            offline_messages = OfflineMessage.objects.filter(user=self.request.user)
            if offline_messages:
                messages.extend(offline_messages)
                offline_messages.delete()

        online_messages, all_retrieved  = super(OfflineStorageEngine, self)._get(*args, **kwargs)
        if online_messages:
            messages.extend(online_messages)

        return messages, True

    def _store(self, messages, *args, **kwargs):
        """ Store messages, but not offline. """
        messages = [msg for msg in messages
                        if not isinstance(msg, OfflineMessage)]
        return super(OfflineStorageEngine, self)._store(messages, *args, **kwargs)
