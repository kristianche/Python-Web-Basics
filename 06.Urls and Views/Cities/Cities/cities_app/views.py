from django.shortcuts import render
from django.http import HttpResponse
from . import models


def index(request):
    return HttpResponse('<h1> Hello World! </h1>')


def city_info(request, city_name):
    cities = models.City.objects.filter(name=city_name).get()

    context = {
        'cities': cities
    }

    return


def cities_list(request):
    cities = models.City.objects.all()

    context = {
        'cities': cities
    }

    return render(request=request, template_name='cities/cities_list.html', context=context)