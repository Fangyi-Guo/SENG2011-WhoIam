#this file should manipulate profile page


from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.http import JsonResponse
from .models import Blood, Book  #hopefully works?
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from datetime import datetime, timezone
from django.db.models import Q
from .forms import BookForm

def home(request):
    return render(request, "bloodprofile/homepage.html")


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
                return render(request, 'bloodprofile/homepage.html', {'result':match})
            else:
                return messages.error(request, "no result found")
        else:
            #output all objects to the page
            return render(request, 'bloodprofile/homepage.html', {'result': Blood.objects.all()})
    else:
        return render(request, 'bloodprofile/homepage.html')

@login_required
def bookBlood(request, id):
    # get beach id
    blood = Blood.objects.get(id = id)
    if Book.objects.filter(blood=blood, userBooked= request.user.username).exists():
        messages.success(request, '*You have already Booked the Blood. Dont book it again unless you delete the old one.')
        return redirect()
    form = BookForm(request.POST)
    if form.is_valid():
        #ratings = request.form['ratings']
        volume = form.cleaned_data['volume']
        user_name = request.user.username
        booking = Book()
        booking.blood = blood
        booking.bookDate = datetime.now(timezone.utc).astimezone()
        booking.userBooked = user_name
        booking.save()
        return redirect('bloodprofile/homepage.html')

    return render(request, 'bloodprofile/homepage.html', {'blood':blood, 'form': form})

