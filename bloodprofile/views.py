#this file should manipulate profile page


from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.http import JsonResponse
from .models import Blood, Book  #hopefully works?
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from datetime import datetime, timezone
from django.db.models import Q

def searchBlood(request):
    if request.method == 'POST':
        ctt = request.POST['content']
        if ctt:
            #only search by blood id or blood type in database
            now=datetime.date.today()
            match = Blood.objects.filter(Q(bloodid__icontains=ctt)|
                                         Q(bloodtype__icontains=ctt)
                                        )
            if match:
                return render(request, 'homepage.html', {'result':match})
            else:
                return messages.error(request, "no result found")
        else:
            #output all objects to the page
            return render(request, 'homepage.html', {'result': Blood.objects.all()})
    else:
        return render(request, 'homepage.html')
<<<<<<< HEAD
#def bookingBlood(request):
=======


>>>>>>> 212aee582d7264ce48a4b03cec51f588575057a6

