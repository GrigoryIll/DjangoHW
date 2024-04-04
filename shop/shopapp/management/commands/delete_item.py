from django.core.management.base import BaseCommand, CommandParser
from shopapp.models import Item


class Command(BaseCommand):
    help = 'Delete item'

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='Item ID')

    def handle(self, *args, **kwargs):
        pk = kwargs.get('pk')
        item = Item.objects.filter(pk=pk).first()
        if item is not None:
            item.delete()
        self.stdout.write(f'{item}')
