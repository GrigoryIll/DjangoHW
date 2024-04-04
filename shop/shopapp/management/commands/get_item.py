from django.core.management.base import BaseCommand, CommandParser
from shopapp.models import Item


class Command(BaseCommand):
    help = 'Get item'

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='Item ID')

    def handle(self, *args, **kwargs):
        pk = kwargs['pk']
        item = Item.objects.filter(pk=pk)
        self.stdout.write(f'{item}')
