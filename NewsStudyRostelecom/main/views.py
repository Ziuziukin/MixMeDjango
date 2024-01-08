from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from .models import *


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
    with open('temp_db/taste.csv', 'r', encoding='utf8', errors='ignore') as file:
        taste = []
        for line in file:
            line = line.replace('\n', '')
            line = line.split(';')
            if line[0] == str(id_taste):
                taste = line
                taste.append(f'main/image/taste/{line[3]}/{line[1]}.jpg')

    context = {'taste_info': taste,
               'page': taste[1],
               'title': f'Mix.Me {taste[1]}'}
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