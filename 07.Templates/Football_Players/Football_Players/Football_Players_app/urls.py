from django.urls import path
from . import views

urlpatterns = [
    path("", views.index),
    path("<str:name>/", views.player_page, name='player-data'),
]