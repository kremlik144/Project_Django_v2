from django.core.management.base import BaseCommand
from ...models import Product
import logging

logger = logging.getLogger(__name__)


class Command(BaseCommand):
    """
    Пример работы с таблицей товаров: Удаление товара
    """
    help = "Delete product by id."

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='Client ID')

    def handle(self, *args, **kwargs):
        pk = kwargs.get('pk')
        product = Product.objects.filter(pk=pk).first()
        if product is not None:
            logger.info(f'Successfully delete product (id={pk}): {product}')
            product.delete()
        else:
            logger.warning(f'Product (id={pk}) don\'t exist!')
        self.stdout.write(f'{product}')
