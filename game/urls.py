from django.urls import path

from .views import game

urlpatterns = [
    path('play/', game.play, name="play"),
    path('home/<int:session_token>', game.home, name="home"),
    path('about/<int:session_token>', game.about, name="about"),
    path('terms/<int:session_token>', game.terms, name="terms"),
    path('help/<int:session_token>', game.help, name="help"),
]