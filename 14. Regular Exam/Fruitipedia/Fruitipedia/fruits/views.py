from django.shortcuts import render, redirect
from .forms import ProfileCreateForm, FruitCreateForm, FruitEditForm, FruitDeleteForm, ProfileEditForm
from.models import Fruit, Profile


'''
•	http://localhost:8000/ - index page
•	http://localhost:8000/dashboard/ - dashboard page
•	http://localhost:8000/create/ - fruit create page
•	http://localhost:8000/<fruitId>/details/ - fruit details page
•	http://localhost:8000/<fruitId>/edit/ - fruit edit page
•	http://localhost:8000/<fruitId>/delete/ - fruit delete page
•	http://localhost:8000/profile/create/ - profile create page
•	http://localhost:8000/profile/details/ - profile details page
•	http://localhost:8000/profile/edit/ - profile edit page
•	http://localhost:8000/profile/delete/ - profile delete page
'''


def index(request):
    return render(request, template_name='common/index.html')


def dashboard(request):
    fruits = Fruit.objects.all()
    context = {
        'fruits': fruits
    }

    return render(request, template_name='common/dashboard.html', context=context)


def fruit_create(request):
    form = FruitCreateForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('dashboard')
    context = {
        'form': form
    }

    return render(request, template_name='fruits/create-fruit.html', context=context)


def fruit_details(request, fruit_id):
    fruit = Fruit.objects.filter(id=fruit_id).get()
    context = {
        'fruit': fruit
    }
    return render(request, template_name='fruits/details-fruit.html', context=context)


def fruit_edit(request, fruit_id):
    fruit = Fruit.objects.filter(id=fruit_id).get()
    form = FruitEditForm(request.POST or None, instance=fruit)
    if form.is_valid():
        form.save()
        return redirect('dashboard')

    context = {
        'fruit': fruit,
        'form': form
    }
    return render(request, template_name='fruits/edit-fruit.html', context=context)


def fruit_delete(request, fruit_id):
    fruit = Fruit.objects.filter(id=fruit_id).get()
    form = FruitDeleteForm(request.POST or None, instance=fruit)
    if form.is_valid():
        form.save()
        return redirect('dashboard')
    context = {
        'form': form,
        'fruit': fruit
    }

    return render(request, template_name='fruits/delete-fruit.html', context=context)


def profile_create(request):
    form = ProfileCreateForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('dashboard')

    context = {
        'form': form
    }

    return render(request, template_name='profile/create-profile.html', context=context)


def profile_details(request):
    profile = Profile.objects.get()
    posts_count = Fruit.objects.all().count()
    context = {
        'posts_count': posts_count,
        'profile': profile
    }

    return render(request, template_name='profile/details-profile.html', context=context)


def profile_edit(request):
    profile = Profile.objects.get()
    form = ProfileEditForm(request.POST or None, instance=profile)
    if form.is_valid():
        form.save()
        return redirect('profile-details')
    context = {
        'form': form
    }
    return render(request, template_name='profile/edit-profile.html', context=context)


def profile_delete(request):
    profile = Profile.objects.get()
    fruits = Fruit.objects.all()
    if request.method == 'POST':
        profile.delete()
        fruits.delete()
        return redirect('index')
    return render(request, template_name='profile/delete-profile.html')