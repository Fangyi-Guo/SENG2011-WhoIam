from .models import Reservation, Book, Blood
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
        fields = ['bookingaddress']
        widget = {
            'bookingaddress': TextInput(attrs={'size': 100, 'title': 'required address'})
        }

class DonateForm(ModelForm):
    class Meta:
        model = Blood
        fields = ['bloodtype', 'volume', 'expdate', 'isTested']
        widget = {
            'bloodtype': TextInput(attrs={'size': 10, 'title': 'your blood type'}),
            'volume': NumberInput(attrs={'title': 'the volume you donate'}),
            'expdate': DateInput(attrs={'title': 'the expire date'}),
            'isTested': TextInput(attrs={})
        }