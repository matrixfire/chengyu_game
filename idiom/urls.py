from django.urls import path
from .views import idiom_game

urlpatterns = [
    path('', idiom_game, name='idiom_game'),
]
