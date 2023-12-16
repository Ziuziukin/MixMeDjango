from django.contrib import admin
from django.urls import path

from . import views



urlpatterns = [
    path('', views.account, name='account'), #страница аккаунта юзера
    path('login/', views.login_user, name='login'), #авторизация пользователя
    path('logout/', views.logout_user, name='logout'), #выход пользователя
    path('registration/', views.registration, name='registration'), #регистрация нового пользователя

]


