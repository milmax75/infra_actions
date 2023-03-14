from django.http import HttpResponse


def index(request):
    return HttpResponse('У меня получилось! Хоть и не сразу :) Я МОЛОДЕЦ!!!')


def second_page(request):
    return HttpResponse('А это вторая страница!')
