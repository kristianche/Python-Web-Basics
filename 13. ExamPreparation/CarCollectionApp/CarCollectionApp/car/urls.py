from django.urls import path, include
from . import views

# 	http://localhost:8000/ - index page
#   http://localhost:8000/catalogue/ - catalogue page
# •	http://localhost:8000/profile/create - profile create page
# •	http://localhost:8000/car/create/ - car create page
# •	http://localhost:8000/car/<car-id>/details/ - car details page
# •	http://localhost:8000/car/<car-id>/edit/ - car edit page
# •	http://localhost:8000/car/<car-id>/delete/ - car delete page
# •	http://localhost:8000/profile/details/ - profile details page
# •	http://localhost:8000/profile/edit/ - profile edit page
# •	http://localhost:8000/profile/delete/

urlpatterns = [
    path('', views.index, name='index'),
    path('catalogue/', views.catalogue, name='catalogue'),
    path('car/', include([
        path('<car_id>/details/', views.car_details, name='car-details'),
        path('<car_id>/edit/', views.car_edit, name='car-edit'),
        path('<car_id>/delete/', views.car_delete, name='car-delete'),
        path('create/', views.car_create, name='car-create'),
    ])),
    path('profile', include([
        path('details/', views.profile_details, name='profile-details'),
        path('edit/', views.profile_edit, name='profile-edit'),
        path('delete/', views.profile_delete, name='profile-delete'),
        path('create/', views.profile_create, name='profile-create')
    ]))
]