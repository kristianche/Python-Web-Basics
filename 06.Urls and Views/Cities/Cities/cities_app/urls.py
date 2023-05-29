from django.urls import path
from Cities.cities_app import views

urlpatterns = [
    path('', views.index),
    path('cities', views.cities_list),
    path('cities/<str:city_name>/', views.city_info)
]