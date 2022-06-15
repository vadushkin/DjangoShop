from django.shortcuts import render
from shop_site.models import Product


def _gives_all_products_filter_price(request) -> list:
    """Возвращает все продукты с сортировкой по цене"""
    products = Product.objects.all().select_related('category').order_by('-price')
    context = {
        'title': 'Магазинчик ~ фильтр по цене продукта',
        'products': products,
    }
    return render(request, 'shop_site/main_page.html', context=context)


def _gives_all_products_filter_name_product(request) -> list:
    """Возвращает все продукты с сортировкой по названию"""
    products = Product.objects.all().select_related('category').order_by('name')
    context = {
        'title': 'Магазинчик ~ фильтр по имени продукта',
        'products': products,
    }
    return render(request, 'shop_site/main_page.html', context=context)


def _gives_all_products_filters_on_category(request, category_name) -> list:
    """Возвращает все продукты с сортировкой по категории"""
    products = Product.objects.all().select_related('category').filter(category_id__name=category_name)
    context = {
        'title': 'Магазинчик ~ фильтр по категории',
        'products': products,
    }
    return render(request, 'shop_site/main_page.html', context=context)
