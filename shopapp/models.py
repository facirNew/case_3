from django.db import models
from django.contrib.auth.models import User


class Product(models.Model):
    name = models.CharField(max_length=32, verbose_name='Название', unique=True)
    description = models.TextField(verbose_name='Описание')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена')
    quantity = models.SmallIntegerField(verbose_name='Доступное количество')
    updated = models.DateTimeField(auto_now=True, verbose_name='Дата изменения')
    available = models.BooleanField(default=True, verbose_name='Есть в наличии')


class Order(models.Model):
    comment_to_order = models.TextField(verbose_name='Комментарии к заказу')
    addres_to = models.CharField(max_length=200, verbose_name='Адрес доставки')
    create = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Заказчик')
    priducts = models.ManyToManyField(Product, verbose_name='Заказанные товары')
