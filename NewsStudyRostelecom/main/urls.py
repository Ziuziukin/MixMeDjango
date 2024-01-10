from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name='home'), #заглавная страница - бренды
    path("brand/", views.tastes_brand, name='brand'), #страница вкусы бренда
    path("taste/<int:id_taste>/", views.taste, name='taste'), #страница конкретного вкуса
    path("inform_app/", views.inform_app, name='inform_app'), #страница о приложении
    path("mix/", views.mix, name='mix'), #страница миксы
    path("for_me/", views.for_me, name='for_me'), #страница обо мне

]


