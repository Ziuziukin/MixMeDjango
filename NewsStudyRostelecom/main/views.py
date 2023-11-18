from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

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

def about(request):
    return HttpResponse('<h1> Страница про нас </h1>')

def contacts(request):
    return HttpResponse('<h1> Контакты </h1>')

def sidebar(request):
    return render(request, 'main/sidebar.html')

def brand(request, brand_name):
    with open('temp_db/taste.csv', 'r', encoding='utf8', errors='ignore') as file:
        tastes = []
        for line in file:
            line = line.replace('\n', '')
            line = line.split(';')
            x = []
            if line[3] == brand_name:
                x.append(line[0])
                x.append(line[1])
                x.append(line[2])
                x.append(line[3])
                x.append(f'main/image/taste/{line[3]}/{line[1]}.jpg')
                tastes.append(x)

    context = {'brand': brand_name,
               'tastes_list': tastes,
               'page': brand_name,
               'title': f'Mix.Me {brand_name}'}

    return render(request, 'main/taste_brand.html', context)

def taste(request, id_taste):
    with open('temp_db/taste.csv', 'r', encoding='utf8', errors='ignore') as file:
        taste = []
        for line in file:
            line = line.replace('\n', '')
            line = line.split(';')
            if line[0] == id_taste:
                taste = line

    context = {'taste_info': taste,
               'page': taste[1],
               'title': f'Mix.Me {taste[1]}'}
    return render(request, 'main/taste.html', context)