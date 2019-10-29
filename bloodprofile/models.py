from django.db import models
from django.contrib.auth.models import User
import numpy as np

class Blood(models.Model):
    bloodid = models.IntegerField(min_length=0)
    bloodtype = models.CharField(max_length=50)
    volume = models.FloatField()
    takendate = models.DateField(("blood taken date"), auto_now=False, auto_now_add=False)
    expdate = models.DateField(("blood expire date"), auto_now=False, auto_now_add=False)#whne to expire
    donor = models.CharField(max_length=50)
    disposeddate = models.DateField(("blood disposed date"), auto_now=False, auto_now_add=False)#when was taken
    isTested = models.BooleanField()

    class Meta:
        unique_together = ["beachname",  "lat", "lng"]
    def __str__(self):
        return self.bloodid

class Reservation(models.Model):
    rsvId = models.IntegerField(min_length=0)
    bloodType = models.CharField(max_length=50)
    rsvVolume = models.FloatField()
    userReserved = models.CharField(max_length=50, null=True)
    rsvDate = models.DateField(("reserve blood date"), auto_now=False, auto_now_add=False)

class Book(models.Model):
    bookDate = models.DateField(("booking date"), auto_now=False, auto_now_add=False)
    blood = models.ForeignKey(Blood, on_delete=models.CASCADE)
    userBooked = models.CharField(max_length=50,null=True)