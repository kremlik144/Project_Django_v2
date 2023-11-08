from django.core.management.base import BaseCommand
from ...models import Order
import logging

logger = logging.getLogger(__name__)


class Command(BaseCommand):
    """
    Пример работы с таблицей заказов: Чтение всех заказов из базы данных
    """
    help = "Get all orders."

    def handle(self, *args, **kwargs):
        orders = Order.objects.all()
        logger.info('Get all orders!')
        self.stdout.write(f'{orders}')
