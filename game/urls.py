from django.urls import path

from .views import game

urlpatterns = [
        path('play/<int:match>', game.core, name="game_core")
]