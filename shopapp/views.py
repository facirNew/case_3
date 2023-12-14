from django.shortcuts import render
from .models import *


def shop_index(request):
    context = {
        'title': 'Главная страница',
    }
    return render(request, 'shopapp/index.html', context)


def products_list(request):
    products = Product.objects.all()
    context = {
        'title': 'Товары',
        'products': products,
    }

    return render(request, 'shopapp/products.html', context=context)


def orders_list(request):
    orders = Order.objects.all().prefetch_related('products').select_related('user_id')
    context = {
        'title': 'Заказы',
        'orders': orders,
    }
    return render(request, 'shopapp/orders.html', context=context)
