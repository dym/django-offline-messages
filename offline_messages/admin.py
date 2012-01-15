from django.contrib import admin

from offline_messages.models import OfflineMessage

class OfflineMessageAdmin(admin.ModelAdmin): 
    list_display = [f.name for f in OfflineMessage._meta.fields]
admin.site.register(OfflineMessage, OfflineMessageAdmin)