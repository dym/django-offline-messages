=========================
Installation Instructions
=========================

Make changes to your settings:

* Add 'offline_messages' to INSTALLED_APPS

* Set MESSAGE_STORAGE to 'offline_messages.storage.OfflineStorageEngine'


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
