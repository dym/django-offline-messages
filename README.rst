.. image::
   https://travis-ci.org/dym/django-offline-messages.png
   :target: https://travis-ci.org/dym/django-offline-messages

.. image::
   https://coveralls.io/repos/dym/django-offline-messages/badge.svg?branch=master&service=github
   :target: https://coveralls.io/github/dym/django-offline-messages?branch=master

.. image:: https://codeclimate.com/github/dym/django-offline-messages/badges/gpa.svg
   :target: https://codeclimate.com/github/dym/django-offline-messages
   :alt: Code Climate

=========================
Installation Instructions
=========================

Make changes to your settings:

* Add 'offline_messages' to INSTALLED_APPS

* Set MESSAGE_STORAGE to 'offline_messages.storage.OfflineStorageEngine'


=========================
About
=========================

This is a slightly modified version of the excellent and simple `offline_messages` package. It
includes generic foreign keys plus extra meta information. This is a specific implementation
for Zapier as we have tons of feedback points, but its easy to confuse the bejesus out of our
customers because important error messages disappear for good.

So basically this adds:

1. Persistent history of messages.
2. Generic foreign keys to attach messages to specific objects (any model, any record).
3. The ability to store even more meta data (EG: the parameters that caused the message).

Enjoy!


=========================
Example Usage
=========================

You can continue to use the standard Django message system as desired. Messages created like:

 from django.contrib import messages
 
 messages.add_message(request, messages.INFO, 'Hello world.')

Will work just fine. However, if you'd like to create an offline message, do something like this:

 from offline_messages.utils import create_offline_message, constants
 
 create_offline_message(User.objects.get(id=1), "Hello there!", level=constants.WARNING)

Or like this:

 from offline_messages.models import OfflineMessage
 
 OfflineMessage.objects.create(user=User.objects.get(id=1), level=20, message='Hello world.')

Usage example from the real life::

 # Iterate through users
 for user in User.objects.all():
     already_notified = OfflineMessage.objects.filter(user=user, message=message).exists()
     if not already_notified:
         create_offline_message(user, message, level=constants.WARNING)

===========================
Extra Functionality
===========================

The idea behind utils is you can just do:

 from offline_messages import utils as messages

In place of:

 from django.contrib import messages

And still have access to boring old `messages.success(request, 'Good job!')` but
also have access to be able to do things like...

 comment = Comment.objects.create(title='A test', message='Thanks!')
 
 messages.success(request, 'Comment posted!', content_object=comment, meta={'blah': 'blah'})

