# -*- coding: utf-8; mode: python; -*-
from django.db import models
from django.contrib.auth.models import User
from django.utils.encoding import force_unicode
from django.contrib.messages import constants
from django.contrib.messages.utils import get_level_tags

class OfflineMessage(models.Model):
    user = models.ForeignKey(User)
    level = models.IntegerField(default=constants.INFO)
    message = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return force_unicode(self.message)

    @property
    def tags(self):
        level_tags = get_level_tags()
        return force_unicode(level_tags.get(self.level, ''), strings_only=True)
