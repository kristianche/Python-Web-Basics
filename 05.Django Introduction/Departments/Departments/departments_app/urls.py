from django.urls import path
from Departments.departments_app.views import sample_view

urlpatterns = [
    path("", sample_view)
]