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

#Вызов страницы для отображения вкусов бренда
def tastes_brand(request):
    with open('temp_db/taste.csv', 'r', encoding='Windows-1251') as file:
        brand_name = request.GET.get("brand_name", 'Вкусы')
        tastes = []
        for line in file:
            line = line.replace('\n', '')
            line = line.split(';')
            x = []
            if brand_name == 'Вкусы':
                x.append(line[0])
                x.append(line[1])
                x.append(line[2])
                x.append(line[3])
                x.append(f'main/image/taste/{line[3]}/{line[1]}.jpg')
                x.append(line[4])
                tastes.append(x)
            elif brand_name != 'all' and line[3] == brand_name:
                x.append(line[0])
                x.append(line[1])
                x.append(line[2])
                x.append(line[3])
                x.append(f'main/image/taste/{line[3]}/{line[1]}.jpg')
                x.append(line[4])
                tastes.append(x)

    context = {'brand': brand_name,
               'tastes_list': tastes,
               'page': brand_name,
               'title': f'Mix.Me {brand_name}'}

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
    return render(request, 'main/inform_app.html')

def page_not_found(request, exception):
    return HttpResponseNotFound('<h1>Ой, что-то пошло не так. Страница не найдена. Теперь есть время перезабить кальян!</h1>')

def mix(request):
    context = {'page': 'Миксы',
               'title': 'Mix.Me'}

    return render(request, 'main/mix.html', context)