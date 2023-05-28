from django.shortcuts import render


def index(request):
    data = {
        'title': 'Головна сторінка',
        'values': ['Швидко', 'Зручно', 'Надійно'],
        'obj': {
            'par_1': '',
            'par_2': '',
            'par_3': ''
        }
    }
    return render(request, 'main/index.html', data)


def about(request):
    data = {
        'title': 'Інформація про нас'
    }
    return render(request, 'main/about.html', data)


def contacts(request):
    data = {
        'title': 'Контактна інформація'
    }
    return render(request, 'main/contacts.html', data)


def news(request):
    data = {
        'title': 'Актуальні новини'
    }
    return render(request, 'main/news.html')


def catalog_views(request):
    data = {
        'title': 'Каталог книжок'
    }
    return render(request, 'main/catalog.html')
