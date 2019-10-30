# pages/urls.py
from django.urls import path

from .views import searchBlood

urlpatterns = [
    path('', views.searchBlood, name='searchBlood')
]
