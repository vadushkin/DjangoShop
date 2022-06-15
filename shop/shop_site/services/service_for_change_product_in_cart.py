from django.db.models import F
from django.http import Http404
from django.shortcuts import redirect, get_object_or_404
from shop_site.models import Product, Cartitem, Cart


def _gives_user_id(user_name) -> int:
    """Отдаёт id пользователя"""
    user_id = Cart.objects.all().filter(user=user_name)[0].pk
    return user_id


def _gives_prod_id(product_name) -> int:
    """Отдаёт id продукта"""
    prod_id = Product.objects.all().filter(name=product_name)[0].pk
    return prod_id


def _gives_user_id_and_prod_id(user_name, product_name) -> list:
    """Возвращает id продукта и пользователя"""
    user_id = _gives_user_id(user_name)
    prod_id = _gives_prod_id(product_name)
    return [user_id, prod_id]


def _add_or_update_product_in_cart(user_name, product_name):
    """Добавляет или создаёт продукт в корзине пользователя"""
    user_id, prod_id = _gives_user_id_and_prod_id(user_name, product_name)
    try:
        cart_item = get_object_or_404(Cartitem, cart_id=user_id, prod_id_id=prod_id, quantity__gt=0)
        cart_item.quantity = F('quantity') + 1
        cart_item.save()
    except Http404:
        Cartitem.objects.create(cart_id=user_id, prod_id_id=prod_id, quantity=1)
    return redirect('cart')


def _delete_product_in_cart(user_name, product_name):
    """Удаляет продукт из корзины пользователя"""
    user_id, prod_id = _gives_user_id_and_prod_id(user_name, product_name)
    Cartitem.objects.filter(cart_id=user_id, prod_id_id=prod_id).delete()
    return redirect('cart')


def _increases_products_in_the_cart(user_name, product_name):
    """Прибавляет один товар в корзину пользователю"""
    user_id, prod_id = _gives_user_id_and_prod_id(user_name, product_name)
    try:
        cart_item = get_object_or_404(Cartitem, cart_id=user_id, prod_id_id=prod_id, quantity__gt=0)
        cart_item.quantity = F('quantity') + 1
        cart_item.save()
    except Http404:
        Cartitem.objects.create(cart_id=user_id, prod_id_id=prod_id, quantity=1)
    return redirect('cart')


def _decreases_products_in_the_cart(user_name, product_name):
    """Убавляет один товар в корзину пользователю"""
    user_id, prod_id = _gives_user_id_and_prod_id(user_name, product_name)
    try:
        cart_item = get_object_or_404(Cartitem, cart_id=user_id, prod_id_id=prod_id, quantity__gt=1)
        cart_item.quantity = F('quantity') - 1
        cart_item.save()
    except Http404:
        Cartitem.objects.filter(cart_id=user_id, prod_id_id=prod_id).delete()
    return redirect('cart')
