from django.core.management.base import BaseCommand
from ...models import Client
import logging

logger = logging.getLogger(__name__)


class Command(BaseCommand):
    """
    Пример работы с таблицей клиентов: Изменение данных об одном конкретном клиенте из базы данных
    """
    help = "Update client name by id."

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='Client ID')
        parser.add_argument('name', type=str, help='Client name')
        parser.add_argument('email', type=str, help='Client email')
        parser.add_argument('phone', type=str, help='Client phone')
        parser.add_argument('address', type=str, help='Client address')

    def handle(self, *args, **kwargs):
        pk = kwargs.get('pk')
        name = kwargs.get('name')
        email = kwargs.get('email')
        phone = kwargs.get('phone')
        address = kwargs.get('address')

        client = Client.objects.filter(pk=pk).first()
        client.name = name
        client.email = email
        client.phone = phone
        client.address = address

        client.save()
        self.stdout.write(f'{client}')
        if client is not None:
            logger.info(f'Successfully update client (id={pk}): {client}')
        else:
            logger.warning(f'Client (id={pk}) don\'t exist!')
        self.stdout.write(f'{client}')
