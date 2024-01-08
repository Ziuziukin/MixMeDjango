from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from .models import *
from users.models import *


#Заглавная страница со списком брендов
def index(request):
    #вызываем модель Brands
    brand = Brands.objects.all().order_by('brand_name')

    context = {'brand_info': brand,
               'page': 'Бренды',
               'title': 'Mix.Me',
               }

    return render(request, 'main/index.html', context)

#Вызов страницы для отображения вкусов бренда или всех вкусов
def tastes_brand(request):
    brand_id = request.GET.get("brand_id", 'Вкусы')
    if brand_id == 'Вкусы':
        tastes = Tastes.objects.all().order_by('name_taste')
        brand = 'Вкусы'
    else:
        tastes = Tastes.objects.filter(brand_id=brand_id).order_by('name_taste')
        brand = Brands.objects.get(id=int(brand_id))

    context = {'brand': brand,
               'tastes_list': tastes,
               'page': brand,
               'title': f'Mix.Me {brand}'}
    return render(request, 'main/tastes_brand.html', context)

#Вызов страницы для отображения конкретного вкуса
def taste(request, id_taste):

    taste = Tastes.objects.get(id=int(id_taste))
    try:
        favorite_taste = Favorite_Taste.objects.get(user_id_favorite=request.user.id, taste_id_favorite=id_taste)
        favorite = favorite_taste.favorite_choices
    except ObjectDoesNotExist:
        favorite = None

    context = {'taste_info': taste,
               'page': taste.name_taste,
               'title': f'Mix.Me {taste.name_taste}',
               'favorite': favorite}

    if request.method == 'POST' and favorite == None:
        favorite_choise = Favorite_Taste.objects.create(user_id_favorite=request.user, taste_id_favorite=Tastes.objects.get(id=int(id_taste)), favorite_choices=request.POST.get('Choise'))
        return render(request, 'main/taste.html', context)
    elif request.method == 'POST' and favorite != None:
        favorite_choise = Favorite_Taste.objects.filter(user_id_favorite=request.user.id, taste_id_favorite=id_taste).update(favorite_choices=request.POST.get('Choise'))
        return render(request, 'main/taste.html', context)

    return render(request, 'main/taste.html', context)

def inform_app(request):
    context = {'page': 'О приложении MixMe',
               'title': f'О приложении Mix.Me'}
    return render(request, 'main/inform_app.html', context)

def page_not_found(request, exception):
    return HttpResponseNotFound('<h1>Ой, что-то пошло не так. Страница не найдена. Теперь есть время перезабить кальян!</h1>')

def mix(request):
    context = {'page': 'Миксы',
               'title': 'Mix.Me'}

    return render(request, 'main/mix.html', context)