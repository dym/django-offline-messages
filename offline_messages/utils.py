# -*- coding: utf-8; mode: python; -*-

try:
    from django.contrib.auth import get_user_model
except ImportError:
    from django.contrib.auth.models import User

    def get_user_model():
        return User

from django.contrib.messages import constants
from django.contrib.messages.api import MessageFailure
try:
    from django.utils.encoding import force_unicode
except ImportError:
    from django.utils.encoding import force_text as force_unicode
from django.contrib.messages.utils import get_level_tags

from offline_messages.models import OfflineMessage

__doc__ = """

The idea here is you can just do:

    from offline_messages import utils as messages

In place of:

    from django.contrib import messages

And still have access to boring old `messages.success(request, 'Good job!')` but
also have access to be able to do things like...

    comment = Comment.objects.create(title='A test', message='Thanks!')
    messages.success(request, 'Comment posted!', content_object=comment, meta={'blah': 'blah'})

""".strip()


def create_offline_message(user,
                           message,
                           level=constants.INFO,
                           read=False,
                           content_object=None,
                           meta={}):

    if not isinstance(user, get_user_model()):
        user = get_user_model().objects.get(username=user)

    level_tags = get_level_tags()
    label_tag = force_unicode(level_tags.get(level, ''), strings_only=True)

    kwargs = dict(
        user=user,
        level=level,
        tags=label_tag,
        read=read,
        message=message,
        meta=dict(meta)
    )

    if content_object:
        kwargs['content_object'] = content_object

    return OfflineMessage.objects.create(**kwargs)


def add_message(request, level, message, extra_tags='', fail_silently=False, **kwargs):
    """
    Attempts to add a message to the request using the 'messages' app, falling
    back to the user's message_set if MessageMiddleware hasn't been enabled.
    """
    if hasattr(request, 'user') and request.user.is_authenticated():
        # can pass in content_object and meta now
        return create_offline_message(request.user, message, level, **kwargs)
    if hasattr(request, '_messages'):
        return request._messages.add(level, message, extra_tags)
    if not fail_silently:
        raise MessageFailure('Without the django.contrib.messages '
                             'middleware, messages can only be added to '
                             'authenticated users.')


def debug(request, message, **kwargs):
    add_message(request, constants.DEBUG, message, **kwargs)


def info(request, message, **kwargs):
    add_message(request, constants.INFO, message, **kwargs)


def success(request, message, **kwargs):
    add_message(request, constants.SUCCESS, message, **kwargs)


def warning(request, message, **kwargs):
    add_message(request, constants.WARNING, message, **kwargs)


def error(request, message, **kwargs):
    add_message(request, constants.ERROR, message, **kwargs)
