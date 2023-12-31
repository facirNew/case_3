# Generated by Django 5.0 on 2023-12-14 12:00

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopapp', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='available',
            field=models.BooleanField(default=True, verbose_name='Есть в наличии'),
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment_to_order', models.TextField(verbose_name='Комментарии к заказу')),
                ('addres_to', models.CharField(max_length=200, verbose_name='Адрес доставки')),
                ('create', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('priducts', models.ManyToManyField(to='shopapp.product', verbose_name='Заказанные товары')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Заказчик')),
            ],
        ),
    ]
