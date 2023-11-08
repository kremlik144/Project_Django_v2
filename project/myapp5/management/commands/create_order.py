from django.core.management.base import BaseCommand
from ...models import Order, Client, Product
import decimal
import logging

logger = logging.getLogger(__name__)


class Command(BaseCommand):
    """
    Пример работы с таблицей заказов: Создание заказа
    """
    help = "Create order."

    def handle(self, *args, **kwargs):
        client_pk = 40  # Выбираем, от какого клиента поступил заказ
        client = Client.objects.filter(pk=client_pk).first()

        # Строим список товаров для заказа
        products = Product.objects.filter(name__contains="Мягкий")

        order = Order(client=client,
                      total_price=decimal.Decimal('321.09'))
        order.save()                  # Сохраняем заказ
        order.products.set(products)  # "Прицепляем" к созданному заказу выбранные товары

        logger.info(f'Successfully create order: {order}')

