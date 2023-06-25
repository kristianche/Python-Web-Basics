from django.urls import path, include
from . import views

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


urlpatterns = [
    path('', views.index, name='index'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('create/', views.fruit_create, name='fruit-create'),
    path('<int:fruit_id>/details/', views.fruit_details, name='fruit-details'),
    path('<int:fruit_id>/edit/', views.fruit_edit, name='fruit-edit'),
    path('<int:fruit_id>/delete/', views.fruit_delete, name='fruit-delete'),
    path('profile/', include([
        path('create/', views.profile_create, name='profile-create'),
        path('details/', views.profile_details, name='profile-details'),
        path('edit/', views.profile_edit, name='profile-edit'),
        path('delete/', views.profile_delete, name='profile-delete'),
    ]))
]