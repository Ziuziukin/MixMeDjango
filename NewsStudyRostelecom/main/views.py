from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound


# Create your views here.

#Заглавная страница со списком брендов
def index(request):
    with open('temp_db/brand_name.csv', 'r', encoding='utf8', errors='ignore') as file:
        brand = []
        for line in file:
            x = []
            line = line.replace('\n', '')
            if line != '':
                x.append(line)
                line = 'main/image/brand_image/' + line + '.jpg'
                x.append(line)
                brand.append(x)

    context = {'brand_info': brand,
               'page': 'Бренды',
               'title': 'Mix.Me'}

    return render(request, 'main/index.html', context)

#Вызов страницы для отображения вкусов бренда
def tastes_brand(request, brand_name):
    with open('temp_db/taste.csv', 'r', encoding='Windows-1251') as file:
        tastes = []
        for line in file:
            line = line.replace('\n', '')
            line = line.split(';')
            print(line)
            x = []
            if line[3] == brand_name:
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

def account(request, id_user):
    context = {'id_user': id_user}
    return render(request, 'main/account.html', context)

def inform_app(request):
    return render(request, 'main/inform_app.html')

def page_not_found(request, exception):
    return HttpResponseNotFound('<h1>Ой, что-то пошло не так. Страница не найдена. Теперь есть время перезабить кальян!</h1>')