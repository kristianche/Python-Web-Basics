from django.shortcuts import render, redirect
from .forms import ProfileCreateForm, CarCreateForm, CarEditForm, CarDeleteForm, ProfileEditForm
from.models import Car, Profile

# 	http://localhost:8000/ - index page
# •	http://localhost:8000/profile/create - profile create page
# •	http://localhost:8000/catalogue/ - catalogue page
# •	http://localhost:8000/car/create/ - car create page
# •	http://localhost:8000/car/<car-id>/details/ - car details page
# •	http://localhost:8000/car/<car-id>/edit/ - car edit page
# •	http://localhost:8000/car/<car-id>/delete/ - car delete page
# •	http://localhost:8000/profile/details/ - profile details page
# •	http://localhost:8000/profile/edit/ - profile edit page
# •	http://localhost:8000/profile/delete/


def index(request):
    return render(request, template_name='common/index.html')


def catalogue(request):
    cars = Car.objects.all()
    context = {
        'cars': cars
    }

    return render(request, template_name='common/catalogue.html', context=context)


def profile_create(request):
    form = ProfileCreateForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('catalogue')

    context = {
        'form': form
    }

    return render(request, template_name='profile-pages/profile-create.html', context=context)


def profile_details(request):
    profile = Profile.objects.get()
    cars = Car.objects.all()
    total_price = 0
    for car in cars:
        total_price += car.price
    context = {
        'profile': profile,
        'total_price': total_price
    }
    return render(request, template_name='profile-pages/profile-details.html', context=context)


def profile_edit(request):
    profile = Profile.objects.get()
    form = ProfileEditForm(request.POST or None, instance=profile)
    if form.is_valid():
        form.save()
        return redirect('profile-details')

    context = {
        'form': form
    }

    return render(request, template_name='profile-pages/profile-edit.html', context=context)


def profile_delete(request):
    profile = Profile.objects.get()
    cars = Car.objects.all()

    if request.method == 'POST':
        profile.delete()
        cars.delete()
        return redirect('index')

    return render(request, 'profile-pages/profile-delete.html')


def car_create(request):
    form = CarCreateForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('catalogue')
    context = {
        'form': form
    }

    return render(request, template_name='cars/car-create.html', context=context)


def car_details(request, car_id):
    car = Car.objects.filter(id=car_id).get()
    context = {
        'car': car
    }

    return render(request, template_name='cars/car-details.html', context=context)


def car_edit(request, car_id):
    car = Car.objects.filter(id=car_id).get()
    form = CarEditForm(request.POST or None, instance=car)
    if form.is_valid():
        form.save()
        return redirect('catalogue')

    context = {
        'car': car,
        'form': form
    }

    return render(request, template_name='cars/car-edit.html', context=context)


def car_delete(request, car_id):
    car = Car.objects.filter(id=car_id).get()
    form = CarDeleteForm(request.POST or None, instance=car)
    if form.is_valid():
        form.save()
        return redirect('catalogue')

    context = {
        'car': car,
        'form': form
    }

    return render(request, template_name='cars/car-delete.html', context=context)


