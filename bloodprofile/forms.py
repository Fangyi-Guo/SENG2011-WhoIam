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
            'rsvDate': DateInput(format='%m/%d/%Y', attrs={'title': 'mm/dd/yyyy'})
            'address': DateInput('size': 100, 'title': 'address')
        }

class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = ['volume']
        widgets = {
		    'volume': forms.Select(attrs={'style': 'cursor: pointer; border-radius:4px; border:0px; box-shadow: 0px 8px 16px 0px rgba(0,0,0,0.2);'})
        }
