from django.core.management.base import BaseCommand, CommandParser
from shopapp.models import Order


class Command(BaseCommand):
    help = 'Get order'

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='Order ID')

    def handle(self, *args, **kwargs):
        pk = kwargs['pk']
        order = Order.objects.filter(pk=pk).first()
        items = order.item.all()
        self.stdout.write(f'{order}: {items}')
