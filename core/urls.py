from django.urls import path, include

from .views import (
    site_index,
    user,
    pre_game
)


urlpatterns = [
    path('', site_index.index, name='index'),
    path('user/index', user.general.index, name="user_index"),
    path('play', pre_game.main.new_math_or_continue, name="new_or_continue")
]