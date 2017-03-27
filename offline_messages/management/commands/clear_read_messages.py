from django.core.management.base import BaseCommand
from offline_messages.models import OfflineMessage


class Command(BaseCommand):
    help = "Deletes all read messages from the database"

    def handle(self, *args, **options):
        read_messages = OfflineMessage.objects.filter(read=True)
        for message in read_messages:
            message.delete()
