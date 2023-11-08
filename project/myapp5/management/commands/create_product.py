from django.core.management.base import BaseCommand
from ...models import Product
import decimal
import logging

logger = logging.getLogger(__name__)


class Command(BaseCommand):
    """
    Пример работы с таблицей товаров: Создание товара
    """
    help = "Create product."

    def add_arguments(self, parser):
        parser.add_argument('name', type=str, help='Product name')
        parser.add_argument('description', type=str, help='Product description')
        parser.add_argument('price', type=str, help='Product\'s price')
        parser.add_argument('amount', type=int, help='Amount of product')

    def handle(self, *args, **kwargs):
        name = kwargs.get('name')
        description = kwargs.get('description')
        price = kwargs.get('price')
        amount = kwargs.get('amount')

        product = Product(name=name, description=description,
                          price=decimal.Decimal(price), amount=amount)
        product.save()
        logger.info(f'Successfully create product: {product}')

