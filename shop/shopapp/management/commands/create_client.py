from django.core.management.base import BaseCommand
from shopapp.models import Client


class Command(BaseCommand):
    help = 'Create client'

    def handle(self, *args, **kwargs):
        client = Client(name='Ivan', email="Ivan@mail.ru",
                        phone='123-15', address='Spb')
        client.save()
        self.stdout.write(f'{client}')
