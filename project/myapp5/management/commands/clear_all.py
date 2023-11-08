from django.core.management.base import BaseCommand
from ...models import Client
from ...models import Product
from ...models import Order

import logging

logger = logging.getLogger(__name__)

class Command(BaseCommand):
    """
    Очистка всех таблиц
    """
    help = "Clear all tables"

    def handle(self, *args, **kwargs):
        orders = Order.objects.all()
        for order in orders:
            order.delete()
        logger.info('Clear all data in Order table!')

        products = Product.objects.all()
        for product in products:
            product.delete()
        logger.info('Clear all data in Product table!')

        clients = Client.objects.all()
        for client in clients:
            client.delete()
        logger.info('Clear all data in Clents table!')
