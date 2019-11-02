# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm
#  from .models import Comment
from django.http import HttpResponse
from bloodprofile.models import Reservation, Book



def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
                form.save()
                username = form.cleaned_data.get('username')
                messages.success(request, 'Your account has been created! You are now able to log in')
                return redirect('/')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})

@login_required
def profile(request):
    user = request.user
    port = request.META['SERVER_PORT']
    reservation_list = Reservation.objects.filter(userReserved = user.username).order_by('-rsvDate')
    book_list = Book.objects.filter(userBooked = user.username).order_by('-bookDate')

    context = {
        'reservation_list':reservation_list,
        'book_list':book_list,
        'port':port
    }
    return render(request, 'users/profile.html',context )



