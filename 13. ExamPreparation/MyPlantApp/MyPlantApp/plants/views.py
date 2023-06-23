from django.shortcuts import render, redirect
from .forms import ProfileCreateForm, PlantCreateForm, PlantBaseForm, PlantEditForm, PlantDeleteForm, ProfileEditForm
from .models import Plant, Profile

'''

•	http://localhost:8000/ - home page
•	http://localhost:8000/profile/create/ - profile create page
•	http://localhost:8000/catalogue/ - catalogue
•	http://localhost:8000/create/ - plant create page
•	http://localhost:8000/details/<plant_id>/ - plant details page
•	http://localhost:8000/edit/<plant_id>/ - plant edit page
•	http://localhost:8000/delete/<plant_id>/ - plant delete page
•	http://localhost:8000/profile/details/ - profile details page
•	http://localhost:8000/profile/edit/ - profile edit page
•	http://localhost:8000/profile/delete/ - profile delete page

'''


def index(request):
    return render(request, template_name='common/home-page.html')


def catalogue(request):
    plants = Plant.objects.all()

    context = {
        'plants': plants
    }

    return render(request, template_name='common/catalogue.html', context=context)


def profile_create(request):
    form = ProfileCreateForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('catalogue')

    context = {
        'form': form,
    }

    return render(request, 'profile/create-profile.html', context=context)


def profile_edit(request):
    profile = Profile.objects.first()
    form = ProfileEditForm(request.POST or None, instance=profile)
    if form.is_valid():
        form.save()
        return redirect('profile-details')

    context = {
        'form': form
    }

    return render(request, template_name='profile/edit-profile.html', context=context)


def profile_details(request):
    plants = Plant.objects.all()
    profile = Profile.objects.first()

    context = {
        'plants': plants,
        'profile': profile
    }

    return render(request, template_name='profile/profile-details.html', context=context)


def profile_delete(request):
    profile = Profile.objects.first()
    plants = Plant.objects.all()
    if request.method == "POST":
        profile.delete()
        plants.delete()
        return redirect('home-page')

    return render(request, template_name='profile/delete-profile.html')


def plant_create(request):
    form = PlantCreateForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('catalogue')

    context = {
        'form': form
    }

    return render(request, template_name='plant/create-plant.html', context=context)


def plant_details(request, plant_id):
    plant = Plant.objects.filter(id=plant_id).get()
    context = {
        'plant': plant
    }

    return render(request, template_name='plant/plant-details.html', context=context)


def plant_edit(request, plant_id):
    plant = Plant.objects.filter(pk=plant_id).get()
    form = PlantEditForm(request.POST or None, instance=plant)
    if form.is_valid():
        form.save()
        return redirect('catalogue')

    context = {
        'form': form,
        'plant': plant
    }

    return render(request, template_name='plant/edit-plant.html', context=context)


def plant_delete(request, plant_id):

    plant = Plant.objects.filter(pk=plant_id).get()
    form = PlantDeleteForm(request.POST or None, instance=plant)
    if form.is_valid():
        form.save()
        return redirect('catalogue')

    context = {
        'form': form,
        'plant': plant
    }

    return render(request, template_name='plant/delete-plant.html', context=context)

