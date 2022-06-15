from .services.service_for_user_registration import _register_user, _login_user, _logout_user
from .services.service_for_gives_products_and_carts_for_user import _gives_all_products, _give_cart_user
from .services.service_for_change_product_in_cart import _delete_product_in_cart, _add_or_update_product_in_cart, \
    _increases_products_in_the_cart, _decreases_products_in_the_cart
from .services.service_for_filters_product import _gives_all_products_filter_name_product, \
    _gives_all_products_filter_price, _gives_all_products_filters_on_category


def home_page(request):
    """Главная страница магазина"""
    return _gives_all_products(request)


def cart_user(request):
    """Показывает корзину определённого пользователя"""
    user_name = request.user
    return _give_cart_user(request, user_name)


def add_product_in_cart(request, product_name):
    """Добавление товара в корзину пользователю"""
    user_name = request.user
    return _add_or_update_product_in_cart(user_name, product_name)


def delete_product_in_cart(request, product_name):
    """Удаление товара из корзины пользователя"""
    user_name = request.user
    return _delete_product_in_cart(user_name, product_name)


def increasing_products_in_the_cart(request, product_name):
    """Прибавление количества товара в корзину пользователю"""
    user_name = request.user
    return _increases_products_in_the_cart(user_name, product_name)


def decreasing_products_in_the_cart(request, product_name):
    """Уменьшение количества товара в корзину пользователю"""
    user_name = request.user
    return _decreases_products_in_the_cart(user_name, product_name)


def filters_products_by_price(request):
    """Фильтрация товаров по цене"""
    return _gives_all_products_filter_price(request)


def filters_products_by_category(request, category_name):
    """Фильтрация товаров по категории"""
    return _gives_all_products_filters_on_category(request, category_name)


def filters_products_by_name(request):
    """Фильтрация товаров по названию товара"""
    return _gives_all_products_filter_name_product(request)


def register_user(request):
    """Регистрация пользователя"""
    return _register_user(request=request)


def login_user(request):
    """Авторизация пользователя"""
    return _login_user(request=request)


def logout_user(request):
    """Выход из учетной записи определённого пользователя"""
    return _logout_user(request=request)
