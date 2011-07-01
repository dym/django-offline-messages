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

 from offline_messages.models import OfflineMessage
 
 OfflineMessage.objects.create( user = User.objects.get(id=1), level = 20, message = 'Hello world.' )