from django.core.management.base import BaseCommand
from .create_client import Command as cC
from .create_product import Command as cP
from ...models import Client, Product, Order
import logging
from faker import Faker
from datetime import timezone, timedelta


logger = logging.getLogger(__name__)


class Command(BaseCommand):
    """
    Генерируем фейковые данные
    """
    help = "Generate fake data"

    def add_arguments(self, parser):
        parser.add_argument('clients', type=int, help='Amount of clients')
        parser.add_argument('products', type=int, help='Amount of products')
        parser.add_argument('orders', type=int, help='Amount of orders')

    def handle(self, *args, **kwargs):
        clients = kwargs.get('clients')
        products = kwargs.get('products')
        orders = kwargs.get('orders')

        fake = Faker(locale="ru_RU")

        # Генерируем фейковых клиентов
        for _ in range(clients):
            cC.handle(self, name=fake.name(), email=fake.email(),
                      phone=fake.phone_number(), address=fake.address())
        logger.info(f'Added {clients} record into table Clients')

        # Генерируем фейковые товары
        for _ in range(products):
            cP.handle(self, name=f'{fake.word().title()} {fake.word()}',
                      description=fake.text().replace('\n', ' '),
                      price=f'{fake.random_int(min=0, max=9999)}.{fake.random_int(min=0, max=99)}',
                      amount=fake.random_int(min=0, max=99))
        logger.info(f'Added {products} record into table Products')

        client_ids = list(Client.objects.values_list('id', flat=True))
        product_ids = list(Product.objects.values_list('id', flat=True))

        # Генерируем фейковые заказы
        for _ in range(orders):
            selected_client = fake.random_choices(elements=client_ids, length=1)
            client = Client.objects.filter(pk=selected_client[0]).first()
            selected_products = list(set(fake.random_choices(elements=product_ids,
                                                             length=fake.random_int(min=0, max=5))))
            products = Product.objects.filter(pk__in=selected_products)
            order = Order(client=client,
                          total_price=f'{fake.random_int(min=0, max=9999)}.{fake.random_int(min=0, max=99)}',
                          order_date=fake.date_time_between('-1y', tzinfo=timezone(timedelta(hours=3), name='МСК')))
            order.save()
            order.products.set(products)

        logger.info(f'Added {orders} record into table Orders')
