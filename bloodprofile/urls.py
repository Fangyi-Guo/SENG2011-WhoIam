# pages/urls.py
from django.urls import path

from .views import searchBlood, home, makeResveration,index,delete_reservation, donate_blood

urlpatterns = [
    path('', home, name='blood-home'),
    path('search', searchBlood, name='blood-search'),
    path('', makeResveration, name='reservation'),
    path('',index, name='index'),
    path('',delete_reservation, name = 'delete_reservation'),
    path('', donate_blood, name='donation')
]
