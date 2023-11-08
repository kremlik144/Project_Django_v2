from django.core.management.base import BaseCommand
from ...models import Product
import logging

logger = logging.getLogger(__name__)


class Command(BaseCommand):
    """
    Пример работы с таблицей товаров: Чтение всех товаров из базы данных
    """
    help = "Get all products."

    def handle(self, *args, **kwargs):
        products = Product.objects.all()
        logger.info('Get all products!')
        self.stdout.write(f'{products}')
