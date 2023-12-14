from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=32, verbose_name='Название', unique=True)
    description = models.TextField(verbose_name='Описание')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена')
    quantity = models.SmallIntegerField(verbose_name='Доступное количество')
    updated = models.DateTimeField(auto_now=True, verbose_name='Дата изменения')
    available = models.BooleanField(default=True)


    # - - [ ] CharField;
    # - - [ ] TextField;
    # - - [ ] DecimalField;
    # - - [ ] PositiveSmallIntegerField;
    # - - [ ] DateTimeField;
    # - - [ ] BooleanField.
