from django import template
from shop_site.models import Category

register = template.Library()


@register.inclusion_tag('shop_site/list_categories.html')
def show_categories():
    categories = Category.objects.order_by('name').distinct()
    return {"categories": categories}


@register.simple_tag()
def multiply(qty, unit_price):
    return qty * unit_price
