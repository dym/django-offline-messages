# -*- coding: utf-8; mode: python; -*-
from django.db import models
from django.contrib.auth.models import User


class OfflineMessage(models.Model):
    user = models.ForeignKey(User)
    message = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return u"%s" % self.message
