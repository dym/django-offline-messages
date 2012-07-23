# -*- coding: utf-8; mode: python; -*-
from django.db import models
from django.contrib.auth.models import User
from django.utils.encoding import force_unicode
from django.contrib.messages import constants
from django.contrib.messages.utils import get_level_tags

from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic

from jsonfield import JSONField


class OfflineMessageQuerySetManager(models.query.QuerySet):
    """ Provide easy to use filters for use in templates
    """

    def info(self):
        return self.filter(level=constants.INFO)

    def debug(self):
        return self.filter(level=constants.DEBUG)

    def success(self):
        return self.filter(level=constants.SUCCESS)

    def warning(self):
        return self.filter(level=constants.WARNING)

    def error(self):
        return self.filter(level=constants.ERROR)

    def unread(self):
        return self.filter(read=False)


class OfflineMessageManager(models.Manager):

    def get_query_set(self):
        return OfflineMessageQuerySetManager(self.model)

    def __getattr__(self, name):
        return getattr(self.get_query_set(), name)


class OfflineMessage(models.Model):
    user = models.ForeignKey(User)
    level = models.IntegerField(default=constants.INFO)
    message = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)

    read = models.BooleanField(default=False)

    content_type = models.ForeignKey(ContentType, blank=True, null=True)
    object_id = models.PositiveIntegerField(blank=True, null=True)
    content_object = generic.GenericForeignKey('content_type', 'object_id')

    meta = JSONField(default={}, blank=True, null=True)

    objects = OfflineMessageManager()

    def __unicode__(self):
        return force_unicode(self.message)

    @property
    def tags(self):
        level_tags = get_level_tags()
        return force_unicode(level_tags.get(self.level, ''), strings_only=True)