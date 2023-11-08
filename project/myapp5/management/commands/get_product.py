from django.core.management.base import BaseCommand
from ...models import Product
import logging

logger = logging.getLogger(__name__)


class Command(BaseCommand):
    """
    Пример работы с таблицей товаров: Чтение одного конкретного товара из базы данных
    """
    help = "Get product by id."

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='Product ID')

    def handle(self, *args, **kwargs):
        pk = kwargs['pk']
        product = Product.objects.filter(pk=pk).first()
        if product is not None:
            logger.info(f'Successfully get product (id={pk}): {product}')
        else:
            logger.warning(f'Product (id={pk}) don\'t exist!')
        self.stdout.write(f'{product}')
