from django.db import models
from django.contrib.auth.models import User
#import numpy as np

class Blood(models.Model):
    #bloodid = models.IntegerField()
    bloodtype = models.CharField(max_length=50)
    volume = models.FloatField()
    takendate = models.DateField(("blood taken date"), auto_now=False, auto_now_add=False)
    expdate = models.DateField(("blood expire date"), auto_now=False, auto_now_add=False)#whne to expire
    donor = models.CharField(max_length=50)
    disposeddate = models.DateField(("blood disposed date"), auto_now=False, auto_now_add=False, null=True)#when was taken

    isTested = models.BooleanField()

class Reservation(models.Model):
    #rsvId = models.IntegerField()
    bloodType = models.CharField(max_length=50)
    rsvVolume = models.FloatField()
    userReserved = models.CharField(max_length=50, null=True, default='')
    rsvDate = models.DateField(("reserve blood date"), auto_now=False, auto_now_add=False)
    address = models.CharField(max_length=60, null=True, default='')

class Book(models.Model):
    bookingaddress = models.CharField(max_length=100, null=True)
    bookDate = models.DateTimeField("booking date")
    blood = models.ForeignKey(Blood, on_delete=models.CASCADE)
    volume = models.FloatField()
    userBooked = models.CharField(max_length=50,null=True)