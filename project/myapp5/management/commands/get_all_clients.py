from django.core.management.base import BaseCommand
from ...models import Client
import logging

logger = logging.getLogger(__name__)


class Command(BaseCommand):
    """
    Пример работы с таблицей клиентов: Чтение всех клиентов из базы данных
    """
    help = "Get all clients."

    def handle(self, *args, **kwargs):
        clients = Client.objects.all()
        logger.info('Get all clients!')
        self.stdout.write(f'{clients}')
