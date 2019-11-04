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
from array import *

def home(request):
    return render(request, "bloodprofile/homepage.html")



def searchBlood(request):
    if request.method == 'GET':
        ctt = request.GET.get('searchResult',False)
        if ctt:
            # sort list by Id
            match = searchlist(ctt)
            #get item in pa
            print(match)
            qs = Blood.objects.filter(id__in=[3,1,8])
            qs_sorted = list()
            for id in match:
                qs_sorted.append(Blood.objects.filter(Q(id=id))[:1].get())
            print(qs_sorted)
            return render(request, 'bloodprofile/homepage.html', {'results':qs_sorted})      
    return render(request, 'bloodprofile/homepage.html')


# make search by volumn donor and type you can add more in if statement 
def searchlist(ctt):
    match = list()
    for blood in Blood.objects.all():
        if checkMatch(blood,ctt):
            match.append(blood.id)
#if only one item no need to sort
    if match:
        if (len(match) > 1): 
            match = sortByType(match,ctt)
    return match

#check if the blood item contain ctt add more if you want 
def checkMatch(blood,ctt):
    if (blood.bloodtype == ctt):
        return True
    elif (ctt.isdigit()):
        if blood.volume > int(ctt):
            return True
        else:
            return False
    elif (blood.donor == ctt):
        return True
    else:
        return False

#simple sort by type 
def sortByType(match,ctt):
    Alist = list()
    Blist = list()
    ABlist = list()
    Olist = list()
    
    for id in match:
        blood = Blood.objects.filter(Q(id=id))[:1].get()
        if (blood.bloodtype == 'A'):
            Alist.append(id)
        elif (blood.bloodtype == 'B'):
            Blist.append(id)
        elif (blood.bloodtype == 'AB'):
            ABlist.append(id)
        elif (blood.bloodtype == 'O'):
            Olist.append(id)

    sortedA =sortByExpDate(Alist)
    sortedB =sortByExpDate(Blist)
    sortedAB =sortByExpDate(ABlist)
    sortedO =sortByExpDate(Olist)

    sortedA.extend(sortedB)
    sortedA.extend(sortedAB)
    sortedA.extend(sortedO)

    return sortedA

        
        

#bubble sort(google it) by ExpireDate no need to check mine it is complex
def sortByExpDate(match):
    sort = list()
    if match:
        array = create2D(match)
        i = 0
        while i < len(match):
            j = 0
            newlen = len(match) - i - 1
            while j < newlen:
                if (array[j][1] < array[j+1][1]): 
                    array[j][0], array[j+1][0] = array[j+1][0], array[j][0]
                    array[j][1], array[j+1][1] = array[j+1][1], array[j][1]
                j+=1
            i+=1
#convert 2d array[0] back to list           
        i = 0        
        while i < len(match): 
            sort.append(array[i][0])
            i+=1

    return sort

#we need this since we compare expdate but sort id 
#and the inner forloop should loop through the array contain both id and expdate
#we also need a index number to sort
def create2D (match):
    array = [[0 for x in range(0)]for y in range(len(match))]
    newMatch = Blood.objects.filter(Q(id__in=match))
    i = 0

    while i < len(match):
        id = match[i]
        blood = Blood.objects.filter(Q(id=id))[:1].get()
        array[i].append(blood.id)
        array[i].append(blood.expdate)
        i=i+1
    return array



@login_required
def bookBlood(request, id):
    # get beach id
    blood = Blood.objects.get(id=id)
    #print(id+"hello")
    #print(blood)
    if Book.objects.filter(blood=blood, userBooked= request.user.username).exists():
        return HttpResponseRedirect("/")
    form = BookForm(request.POST)
    if form.is_valid():
        #ratings = request.form['ratings']
        address=form.cleaned_data['bookingaddress']
        user_name = request.user.username

        booking = Book()
        booking.bookingaddress = address
        booking.blood = blood
        blood.isBooked = True
        booking.bookDate = datetime.now(timezone.utc).astimezone()
        booking.userBooked = user_name
        booking.save()
        blood.save()
        return redirect('bloodprofile/homepage.html')

    return render(request, 'bloodprofile/booking.html', {'blood':blood,'form':form})

@login_required
def makeResveration(request):
    user_name = request.user.username
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
            res.userReserved = user_name
            res.save()
            return render(request, 'bloodprofile/Reservation.html', {'success':"success"})

    return render(request, 'bloodprofile/Reservation.html', {'form': form},RequestContext(request))

def index(request):
    
    submitbutton= request.POST.get('Home')

    if submitbutton:
        # execute this code
    
        context= {'submitbutton': submitbutton}

        
    return render(request, 'Articles/index.html', context)


def delete_reservation(request, id):#reservation id
    re = Reservation.objects.filter(id=id)
    bk = Book.objects.filter(userBooked=request.user.username)
    re.delete()
    user = request.user
    port = request.META['SERVER_PORT']
    rsvlist = Reservation.objects.filter(userReserved=user.username).order_by('-rsvDate')
    context = {
        'reservation_list':rsvlist,
        'port':port,
        'book_list': bk
    }
    return render(request, 'users/profile.html',context)
