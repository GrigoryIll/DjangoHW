from django.core.management.base import BaseCommand, CommandParser
from shopapp.models import Item


class Command(BaseCommand):
    help = 'Update item'

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='Client ID')
        parser.add_argument('price', type=float, help='Client name')

    def handle(self, *args, **kwargs):
        pk = kwargs.get('pk')
        price = kwargs.get('price')
        item = Item.objects.filter(pk=pk).first()
        item.price = price
        item.save()
        self.stdout.write(f'{item}')
