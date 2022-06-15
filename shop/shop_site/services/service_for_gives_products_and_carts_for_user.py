from typing import Union
from django.shortcuts import redirect, render
from shop_site.models import Product, Cartitem


def _gives_all_products(request) -> list:
    """Возвращает все продукты"""
    products = Product.objects.all().select_related('category').order_by('-created_at')
    context = {
        'title': 'Магазинчик',
        'products': products,
    }
    return render(request, 'shop_site/main_page.html', context=context)


def _give_cart_user(request, user_name) -> Union[list, None]:
    """Возвращает корзину пользователю"""
    if str(user_name) == 'AnonymousUser':
        return redirect('register')
    cart_items = Cartitem.objects.all().filter(cart__user=user_name).select_related('prod_id')
    context = {
        'title': 'Корзина',
        'cart_item': cart_items,
    }
    return render(request, 'shop_site/cart.html', context=context)
