from .models import Reservation, Book
from django import forms
from django.forms import ModelForm, NumberInput, TextInput, DateInput
from django import forms

class ReserveForm(ModelForm):
    class Meta:
        model = Reservation
        fields = ['bloodType', 'rsvVolume', "rsvDate", "address"]
        widgets = {
		    'bloodType': TextInput(attrs={'size': 10, 'title': 'Blood Type'}),
            'rsvVolume': NumberInput(attrs={'title': 'reserved volume'}),
            'rsvDate': DateInput(format='%m/%d/%Y', attrs={'title': 'mm/dd/yyyy'}),
            'address':TextInput(attrs={'size': 100, 'title': 'required address'})
        }

class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = ['volume', 'bookingaddress']
        widget = {
            'volume': NumberInput(attrs={'title': 'booked volume'}),
            'bookingaddress': TextInput(attrs={'size': 100, 'title': 'required address'})
        }