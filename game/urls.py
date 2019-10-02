from django.urls import path

from .views import game

urlpatterns = [
    path('play/<int:session_token>', game.core, name="play")
]