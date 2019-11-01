#this file should manipulate profile page


from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.http import JsonResponse
from .models import Blood, Book, Reservation  #hopefully works?
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from datetime import datetime, timezone
from django.db.models import Q
from .forms import BookForm, ReserveForm
import datetime as dt
from django.views.decorators.csrf import csrf_protect
from django.template import RequestContext

def home(request):
    return render(request, "bloodprofile/homepage.html")



def searchBlood(request):
    if request.method == 'GET':
        ctt = request.GET.get('searchResult',False)
        if ctt:
            #only search by blood id or blood type or volume or expire date in database
            #YYYY-MM-DD
            now=dt.date.today()
            isValidDate = False
            if('-' in ctt):
                isValidDate = True
            
            if(isValidDate):
                match = Blood.objects.filter(expdate__gte=ctt)
            else:
                match = Blood.objects.filter(Q(id__icontains=ctt)|Q(bloodtype__icontains=ctt)|Q(volume__gte=ctt))
            
            if match:
                return render(request, 'bloodprofile/homepage.html', {'results':match})
            else:
                return render(request, 'bloodprofile/homepage.html',{'error': "no matching result"})
        else:
            #output all objects to the page
            return render(request, 'bloodprofile/homepage.html', {'results': Blood.objects.all()})
    else:
        return render(request, 'bloodprofile/homepage.html')

#@login_required
def bookBlood(request, id):
    # get beach id
    blood = Blood.objects.get(id=id)
    #print(id+"hello")
    #print(blood)
    if Book.objects.filter(blood=blood, userBooked= request.user.username).exists():
        messages.success(request, '*You have already Booked the Blood. Dont book it again unless you delete the old one.')
        return HttpResponseRedirect("/")
    form = BookForm(request.POST)
    if form.is_valid():
        #ratings = request.form['ratings']
        volume = form.cleaned_data['volume']
        if(volume > blood.volume):
             messages.success(request, '*this blood does not have so much amount of blood.')
             return render(request, 'bloodprofile/booking.html', {'blood':blood, 'form':form})
        address=form.cleaned_data['bookingaddress']
        user_name = request.user.username

        booking = Book()
        booking.bookingaddress = address
        booking.volume=volume
        booking.blood = blood
        booking.bookDate = datetime.now(timezone.utc).astimezone()
        booking.userBooked = user_name
        booking.save()
        return redirect('bloodprofile/homepage.html')

    return render(request, 'bloodprofile/booking.html', {'blood':blood,'form':form})

def makeResveration(request):
    # if this is a POST request we need to process the form data
    form = ReserveForm(request.POST)
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        # check whether it's valid:
        if form.is_valid():
            res = Reservation()
            res.bloodType = form.cleaned_data['bloodType']
            res.rsvVolume = form.cleaned_data['rsvVolume']
            res.address = form.cleaned_data['address']
            res.rsvDate = form.cleaned_data['rsvDate']
            #res.userReserved = request.user
            res.save()
            return render(request, 'bloodprofile/Reservation.html', {'success':"success"})

    return render(request, 'bloodprofile/Reservation.html', {'form': form},RequestContext(request))

def index(request):
    
    submitbutton= request.POST.get('Home')

    if submitbutton:
        # execute this code
    
        context= {'submitbutton': submitbutton}

        
    return render(request, 'Articles/index.html', context)
