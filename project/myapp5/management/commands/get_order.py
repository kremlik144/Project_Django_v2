from django.core.management.base import BaseCommand
from ...models import Order
import logging

logger = logging.getLogger(__name__)


class Command(BaseCommand):
    """
    Пример работы с таблицей заказов: Чтение одного конкретного заказа из базы данных
    """
    help = "Get order by id."

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='Order ID')

    def handle(self, *args, **kwargs):
        pk = kwargs['pk']
        order = Order.objects.filter(pk=pk).first()
        if order is not None:
            logger.info(f'Successfully get order (id={pk}): {order}')
        else:
            logger.warning(f'Order (id={pk}) don\'t exist!')
        self.stdout.write(f'{order}')
