from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import *
from .forms import LoginUserForm
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.contrib.auth.forms import UserCreationForm

#функция авторизации пользователя
def login_user(request):
    if request.method == 'POST':
        form = LoginUserForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, username=cd['username'],
                                password=cd['password'])
            if user and user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('home'))
    else:
        form = LoginUserForm()
    return render(request, 'users/login.html', {'form': form})

#функция выхода пользователя из приложения
def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))

#функция отображения информации ЛК пользователя
def account(request):
    user_acc = Account.objects.get(user=request.user)
    context = {'user_info': user_acc,
               }
    return render(request, 'users/account.html', context=context)
