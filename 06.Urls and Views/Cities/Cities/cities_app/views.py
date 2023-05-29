from django.shortcuts import render
from django.http import HttpResponse
from . import models


def index(request):
    return HttpResponse('<h1> Hello World! </h1>')


def city_info(request, city_name):
    city = models.City.objects.filter(name=city_name).get()

    context = {
        'city': city
    }

    return render(request=request, template_name='cities/cities_info_by_name.html', context=context)


def cities_list(request):
    cities = models.City.objects.all()

    context = {
        'cities': cities
    }

    return render(request=request, template_name='cities/cities_list.html', context=context)