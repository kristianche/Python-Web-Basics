from django.urls import path, include
from . import views


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


urlpatterns = [
    path('', views.index, name='home-page'),
    path('catalogue/', views.catalogue, name='catalogue'),
    path('profile/', include([
        path('create/', views.profile_create, name='profile-create'),
        path('details/', views.profile_details, name='profile-details'),
        path('edit/', views.profile_edit, name='profile-edit'),
        path('delete/', views.profile_delete, name='profile-delete')
    ])),
    path('create/', views.plant_create, name='plant-create'),
    path('details/<plant_id>', views.plant_details, name='plant-details'),
    path('edit/<plant_id>', views.plant_edit, name='plant-edit'),
    path('delete/<plant_id>', views.plant_delete, name='plant-delete')
]