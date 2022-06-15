from django.urls import path
from .views import *

urlpatterns = [
    path('', home_page, name='home'),
    path('register/', register_user, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('cart/', cart_user, name='cart'),
    path('price/', filters_products_by_price, name='price'),
    path('name/', filters_products_by_name, name='name'),
    path('category/<str:category_name>', filters_products_by_category, name='category'),
    path('add-product/<str:product_name>/', add_product_in_cart, name='add-product'),
    path('delete-product/<str:product_name>/', delete_product_in_cart, name='delete-product'),
    path('plus-product/<str:product_name>/', increasing_products_in_the_cart, name='plus-product'),
    path('minus-product/<str:product_name>/', decreasing_products_in_the_cart, name='minus-product'),
]
