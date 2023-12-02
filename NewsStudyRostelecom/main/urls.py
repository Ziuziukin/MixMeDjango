from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name='home'), #заглавная страница - бренды
    path("brand/", views.tastes_brand, name='brand'), #страница вкусы бренда
    path("taste/<int:id_taste>/", views.taste, name='taste'), #страница конкретного вкуса
    path("account/<int:id_user>", views.account, name='account'), #страница профиля пользователя
    path("inform_app/", views.inform_app, name='inform_app'), #страница о приложении
    path("mix/", views.mix, name='mix'), #страница миксы

]


