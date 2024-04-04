from django.core.management.base import BaseCommand
from shopapp.models import Order, Client, Item


class Command(BaseCommand):
    help = 'Create order'

    def add_arguments(self, parser):
        parser.add_argument('pk_client', type=int, help='Client ID')
        parser.add_argument('pk_item', nargs='+', type=int, help='Item ID')

    def handle(self, *args, **kwargs):
        pk_client = kwargs.get('pk_client')
        pk_item = kwargs.get('pk_item')
        client = Client.objects.filter(pk=pk_client).first()

        order = Order(client=client, total_sum=0)
        order.save()

        total_sum = 0
        for pk_item_id in pk_item:
            item = Item.objects.filter(pk=pk_item_id).first()
            order.item.add(item)
            total_sum += item.price
        order.total_sum = total_sum
        order.save()
        self.stdout.write(f'{order}')
