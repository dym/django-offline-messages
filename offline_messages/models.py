# -*- coding: utf-8; mode: python; -*-
from django.db import models
from django.contrib.auth.models import User
from django.utils.encoding import force_unicode
from django.contrib.messages import constants

class OfflineMessage(models.Model):
    user = models.ForeignKey(User)
    level = models.IntegerField(default=constants.INFO)
    tags = models.CharField(max_length=100, null=True, blank=True)
    message = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return force_unicode(self.message)
