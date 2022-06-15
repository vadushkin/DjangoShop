from django.contrib import admin
from .models import Product, Category, Cart, Cartitem


class ProductInline(admin.TabularInline):
    model = Product


class CartItemInline(admin.TabularInline):
    model = Cartitem


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', ]
    prepopulated_fields = {'slug': ("name",)}
    inlines = [ProductInline, ]


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'category', 'price', 'created_at', ]
    sortable_by = ['price', 'category']


class CartItemAdmin(admin.ModelAdmin):
    list_display = ['cart', 'prod_id', 'quantity']
    ordering = ['-cart', 'prod_id']


class CartAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', ]
    inlines = [CartItemInline, ]
    ordering = ['id', 'user']


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Cartitem, CartItemAdmin)
admin.site.register(Cart, CartAdmin)
