"""whoiam URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from bloodprofile import views as blood_view



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('bloodprofile.urls')),
<<<<<<< HEAD
    url(r'^(?P<bloodid>\d+)/book_blood/', blood_view.bookBlood, name='blood-booking'),
    url(r'/reservation/', blood_view.makeResveration, name='reservation')
=======
    url(r'^(?P<id>\d+)/blood_booking/', blood_view.bookBlood, name='blood-booking')
>>>>>>> 8eb7ff2be8b2b667be40412ce47aef444702d170
    #url(r'beachProfile/', blood_view.bloodProfile, name='beachProfile'),
]
