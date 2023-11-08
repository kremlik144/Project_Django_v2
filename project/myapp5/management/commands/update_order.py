from django.core.management.base import BaseCommand
from ...models import Order
import logging
import decimal

logger = logging.getLogger(__name__)


class Command(BaseCommand):
    """
    Пример работы с таблицей заказов: Изменение данных об одном конкретном заказе из базы данных
    """
    help = "Update order name by id."

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='Order ID')
        parser.add_argument('total_price', type=decimal.Decimal, help='Order total price')

    def handle(self, *args, **kwargs):
        pk = kwargs.get('pk')
        total_price = kwargs.get('total_price')
        order = Order.objects.filter(pk=pk).first()
        order.total_price = decimal.Decimal(total_price)
        order.save()
        self.stdout.write(f'{total_price}')
        if order is not None:
            logger.info(f'Successfully update order (id={pk}): {order}')
        else:
            logger.warning(f'Order (id={pk}) don\'t exist!')
        self.stdout.write(f'{order}')
