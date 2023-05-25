from django.urls import path
from djangoProject.departments import views

urlpatterns = [
    path("", views.index)
]