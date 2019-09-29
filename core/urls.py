from django.urls import path, include

from .views import (
    site_index,
    user
)


urlpatterns = [
    path('', site_index.index, name='index'),
    path('user/index', user.general.index, name="user_index")
]