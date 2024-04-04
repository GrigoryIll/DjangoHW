from django.core.management.base import BaseCommand
from shopapp.models import Order, Client, Item


class Command(BaseCommand):
    help = 'Update order'

    def add_arguments(self, parser):
        parser.add_argument('pk_order', type=int, help='Order ID')
        parser.add_argument('date', type=str, help='Order data')

    def handle(self, *args, **kwargs):
        pk_order = kwargs.get('pk_order')
        date = kwargs.get('date')
        order = Order.objects.filter(pk=pk_order).first()
        order.date = date
        order.save()
        self.stdout.write(f'{order}')
