from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    objects = models.Manager()
    name = models.CharField(max_length=60, verbose_name='Название')
    slug = models.SlugField(max_length=60, verbose_name='Слаг')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Product(models.Model):
    objects = models.Manager()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')
    name = models.CharField(max_length=100, verbose_name='Название')
    description = models.TextField(verbose_name='Описание', blank=True)
    cover = models.ImageField(upload_to='product/', verbose_name='Фотография')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Время публикации')
    price = models.PositiveIntegerField(verbose_name='Цена')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'


class Cart(models.Model):
    objects = models.Manager()
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='Корзина')

    def __str__(self):
        return f'{self.user}'

    class Meta:
        verbose_name = 'Корзина посетителей'
        verbose_name_plural = 'Корзины посетителей'


class Cartitem(models.Model):
    objects = models.Manager()
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, verbose_name='Корзина')
    prod_id = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Продукт')
    quantity = models.PositiveIntegerField(verbose_name='Количество')

    def __str__(self):
        return f"{self.cart}"

    class Meta:
        verbose_name = 'Товар в корзине'
        verbose_name_plural = 'Товары в корзинах'
