from django.core.management.base import BaseCommand
from shopapp.models import Item


class Command(BaseCommand):
    help = 'Create item'

    def handle(self, *args, **kwargs):
        item = Item(name='Item3', description='Des3',
                    price=15.1, quantity=1)
        item.save()
        self.stdout.write(f'{item}')
