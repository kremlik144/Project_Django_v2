from django.db import models
import datetime

# Create your models here.


class Client(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=150)
    register_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Name: \'{self.name}\', email: {self.email}, address: \'{self.address}\''


class Product(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    amount = models.IntegerField(default=1)
    image = models.CharField(max_length=255, blank=True)
    create_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Name:{self.name}, Description: {self.description}, Price: {self.price}'


class Order(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    total_price = models.DecimalField(max_digits=8, decimal_places=2)
    order_date = models.DateTimeField(default=datetime.datetime.now())

    def __str__(self):
        return f'Client: {self.client}, Product[s]: {self.products.all().values_list()}, Order_date: {self.order_date}'
