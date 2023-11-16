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

    context = {'brand_info': brand}
    return render(request, 'main/index.html', context)

def about(request):
    return HttpResponse('<h1> Страница про нас </h1>')

def contacts(request):
    return HttpResponse('<h1> Контакты </h1>')

def sidebar(request):
    return render(request, 'main/sidebar.html')

def brand(request, brand_name):
    with open('temp_db/taste.csv', 'r', encoding='utf8', errors='ignore') as file:
        taste = []
        for line in file:
            line = line.replace('\n', '')
            line = line.split(';')
            x = []
            if line[2] == brand_name:
                x.append(line[0])
                x.append(line[1])
                x.append(line[2])
                x.append(f'main/image/taste/{line[2]}/{line[0]}.jpg')
                taste.append(x)
        print(len(taste))
        print(taste)

    context = {'brand': brand_name,
               'taste_info': taste}

    return render(request, 'main/taste_brand.html', context)


