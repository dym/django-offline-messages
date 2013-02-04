from django.core.management.base import BaseCommand
from offline_messages.models import OfflineMessage, OfflineExpiration
from datetime import datetime


class Command(BaseCommand):
    help = "Marks all messages that are attacted to expired OfflineExpiration objects as read"

    def handle(self, *args, **options):
        expired_objects = OfflineExpiration.objects.earliest('datetime').all()
        now = datetime.now()
        for expired in expired_objects:
            if expired > now:
                break
            expired_messages = OfflineMessage.objects.filter(content_object=expired)
            for message in expired_messages:
                message.read()
                message.save()
