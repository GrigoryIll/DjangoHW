from django.core.management.base import BaseCommand, CommandParser
from shopapp.models import Client


class Command(BaseCommand):
    help = 'Get client'

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='Client ID')

    def handle(self, *args, **kwargs):
        pk = kwargs['pk']
        client = Client.objects.filter(pk=pk)
        self.stdout.write(f'{client}')
