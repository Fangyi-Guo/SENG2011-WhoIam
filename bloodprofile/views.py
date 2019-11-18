#this file should manipulate profile page


from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.http import JsonResponse
from .models import Blood, Book, Reservation  #hopefully works?
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from datetime import datetime, timezone
from django.db.models import Q
from .forms import BookForm, ReserveForm, DonateForm
import datetime as dt
from django.views.decorators.csrf import csrf_protect
from django.template import RequestContext
from array import *

#home page 
def home(request):
    return render(request, "bloodprofile/homepage.html")

#searching method 
@login_required
def searchBlood(request):
    if request.method == 'GET':
        #ctt user input 
        ctt = request.GET.get('searchResult',False)
        if ctt:
            match = searchlist(ctt)
            return render(request, 'bloodprofile/homepage.html', {'results':match})      
    return render(request, 'bloodprofile/homepage.html')


#check if the blood item contain user input (key word)
#customer can search by type, volume (all the blood itmes have more than require volume are added to match), and donor 
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

#three method pass in a list of blood items display sorted blood list after customer select sorted method  
#init search have no order we will let customer to choose sort method (display all match reault with no order)
#make search by volumn donor and type do we need more searching field?  
def searchlist(ctt):
    match = list()
    for blood in Blood.objects.all():
        if checkMatch(blood,ctt):
            #matching result 
            match.append(blood)
    if match:
        #if only one item no need to sort
        if (len(match) > 1): 
            #match = sortByVolumn(match)
            #match = sortByType(match)
            match = sortByExpDate(match)
    return match

#use list to sort by type 
def sortByType(match):

    Alist = list()
    Blist = list()
    ABlist = list()
    Olist = list()
    
    for blood in match:
        if (blood.bloodtype == 'A'):
            Alist.append(blood)
        elif (blood.bloodtype == 'B'):
            Blist.append(blood)
        elif (blood.bloodtype == 'AB'):
            ABlist.append(blood)
        elif (blood.bloodtype == 'O'):
            Olist.append(blood)

    Alist.extend(Blist)
    Alist.extend(ABlist)
    Alist.extend(Olist)

    return Alist
       

#bubble sort by Expire date 
def sortByExpDate(match):
    sort = list()
    i = 0
    while i < len(match):
        j = 0
        newlen = len(match) - i - 1
        while j < newlen:
            if (match[j].expdate < match[j+1].expdate): 
                match[j], match[j+1] = match[j+1], match[j]
            j+=1
        i+=1        
    return match


#insertion sort by volumn  
def sortByVolumn(match): 
    i = 1
    while i < len(match):
        if match[i].volume < match[0].volume:
            match[0],match[i]=match[i],match[0]
        i+=1

    i = 1
    while i < len(match):
        j = i
        v = match[i]
        while v.volume < match[j-1].volume:
            match[j] = match[j-1]
            j = j -1
        match[j] = v
        i += 1
    #print(match)
    return match

    
#book blood it is like checkout of blood item
#book one blood item one time
#set isBooked attribut to be true and add booked to user's booked list 
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

#make reservation let customer request for a certain amount of blood 
#customers can specify the date they want to receive reservated blood
#create new reservation form and add to \admin 
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

#redirect to home page 
def index(request):
    
    submitbutton= request.POST.get('Home')

    if submitbutton:
        # execute this code
        context= {'submitbutton': submitbutton}
   
    return render(request, 'Articles/index.html', context)

#delete a exist reservation
#delete exist blood form in /admin(django)
def delete_reservation(request, id):
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

#customer donate blood
#create a blood form and add to /admin(django)
@login_required
def donate_blood(request):
    user_name = request.user.username
    print(request)
    # if this is a POST request we need to process the form data
    form = DonateForm(request.POST)
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        # check whether it's valid:
        if form.is_valid():
            blood = Blood()
            blood.bloodtype = str(form.cleaned_data['bloodtype'])
            blood.volume = form.cleaned_data['volume']
            blood.takendate = form.cleaned_data['takendate']
            blood.expdate = blood.takendate + dt.timedelta(days=35)
            blood.donor = user_name
            blood.isBooked = False
            print("inside here hahahahahahhah!\n")
            
            blood.isTested = request.POST.get('isTested', '') == 'on'
            blood.save()
            return render(request, 'bloodprofile/Donation.html', {'success':"success"})

    return render(request, 'bloodprofile/Donation.html', {'form': form},RequestContext(request))
