# -*- coding: utf-8; mode: python -*-
from django.contrib.auth.models import User

from offline_messages.models import OfflineMessage


def create_offline_message(user, message):
    if not isinstance(user, User):
        user = User.objects.get(username=user)

    OfflineMessage.objects.create(user=user, message=message)
