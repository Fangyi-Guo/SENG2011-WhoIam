# pages/urls.py
from django.urls import path

from .views import searchBlood, home, makeResveration

urlpatterns = [
    path('', home, name='blood-home'),
    path('search', searchBlood, name='blood-search'),
    path('', makeResveration, name='reservation')
]
