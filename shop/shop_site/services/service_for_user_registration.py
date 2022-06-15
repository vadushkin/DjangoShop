from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, logout
from shop_site.forms import UserRegisterForm, UserLoginForm
from shop_site.models import Cart


def _register_user(request):
    """Регистрация пользователя"""
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request=request, message='Вы успешно зарегистрировались')
            login(request=request, user=user)
            Cart.objects.create(user=user)
            return redirect('home')
        else:
            messages.error(request=request, message='Ошибка регистрации')
    else:
        form = UserRegisterForm()
    return render(request=request, template_name='shop_site/register.html', context={'form': form})


def _login_user(request):
    """Авторизация пользователя"""
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request=request, user=user)
            messages.success(request=request, message='Вы успешно зашли')
            return redirect('home')
        else:
            messages.error(request=request, message='Ошибка авторизации')
    else:
        form = UserLoginForm()
    return render(request=request, template_name='shop_site/login.html', context={'form': form})


def _logout_user(request):
    """Выход из учетной записи пользователя"""
    logout(request=request)
    return redirect('home')
