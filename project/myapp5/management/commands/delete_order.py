from django.core.management.base import BaseCommand
from ...models import Order
import logging

logger = logging.getLogger(__name__)


class Command(BaseCommand):
    """
    Пример работы с таблицей заказов: Удаление заказа
    """
    help = "Delete order by id."

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='Order ID')

    def handle(self, *args, **kwargs):
        pk = kwargs.get('pk')
        order = Order.objects.filter(pk=pk).first()
        if order is not None:
            logger.info(f'Successfully delete order (id={pk}): {order}')
            order.delete()
        else:
            logger.warning(f'Order (id={pk}) don\'t exist!')
        self.stdout.write(f'{order}')