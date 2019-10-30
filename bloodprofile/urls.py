# pages/urls.py
from django.urls import path

from .views import searchBlood, home

urlpatterns = [
    path('', home, name='blood-home'),
    path('search', searchBlood, name='blood-search')
]
