# -*- coding: utf-8; mode: python; -*-
from django.contrib.auth.models import User
from django.contrib.messages import constants
from django.utils.encoding import force_unicode
from django.contrib.messages.utils import get_level_tags

from offline_messages.models import OfflineMessage


def create_offline_message(user, message, level=constants.INFO):
    if not isinstance(user, User):
        user = User.objects.get(username=user)

    level_tags = get_level_tags()
    label_tag = force_unicode(level_tags.get(level, ''), strings_only=True)

    OfflineMessage.objects.create(user=user,
                                  level=level,
                                  tags=label_tag,
                                  message=message)
