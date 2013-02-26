from django.core.management.base import BaseCommand
from offline_messages.models import OfflineMessage, OfflineExpiration
from datetime import datetime
from django.utils.timezone import utc
from django.contrib.contenttypes.models import ContentType


class Command(BaseCommand):
    help = "Marks all messages that are attacted to expired OfflineExpiration objects as read"

    def handle(self, *args, **options):
        expired_objects = OfflineExpiration.objects.order_by('datetime').all()
        now = datetime.utcnow().replace(tzinfo=utc)
        for expired in expired_objects:
            if expired.datetime > now:
                break
            expired_messages = OfflineMessage.objects.filter(content_type=ContentType.objects.get_for_model(expired),object_id=expired.id)
            for message in expired_messages:
                message.read = True
                message.save()
            expired.delete()
