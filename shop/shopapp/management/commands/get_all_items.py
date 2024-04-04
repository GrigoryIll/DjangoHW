from django.core.management.base import BaseCommand
from shopapp.models import Item


class Command(BaseCommand):
    help = 'Get all items'

    def handle(self, *args, **kwargs):
        items = Item.objects.all()
        self.stdout.write(f'{items}')
