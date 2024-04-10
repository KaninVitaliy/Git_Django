import datetime
import os

from django.http import HttpResponse
from django.shortcuts import render, reverse


def home_view(request):
    template_name = 'app/home.html'
    # впишите правильные адреса страниц, используя
    # функцию `reverse`
    pages = {
        'Главная страница': reverse('home'),
        'Показать текущее время': reverse(time_view),
        'Показать содержимое рабочей директории': reverse(workdir_view),
    }
    
    # context и параметры render менять не нужно
    # подбробнее о них мы поговорим на следующих лекциях
    context = {
        'pages': pages
    }
    return render(request, template_name, context)


def time_view(request):
    # обратите внимание – здесь HTML шаблона нет, 
    # возвращается просто текст
    current_time = datetime.datetime.now().time()
    msg = (f'Текущее время: {current_time}<br />'
           f'<a href="http://127.0.0.1:8000">Главная страница</a>')
    return HttpResponse(msg)


def workdir_view(request):
    dir_name = (f"{(' ; ').join(os.listdir())}<br />"
                f'<a href="http://127.0.0.1:8000">Главная страница</a>')
    return HttpResponse(dir_name)
