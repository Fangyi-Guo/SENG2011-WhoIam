from .models import Reservation
from django import forms
from django.forms import ModelForm, NumberInput, TextInput, DateInput
from django import forms

class ReserveForm(ModelForm):
    class Meta:
        model = Reservation
        fields = ['bloodType', 'rsvVolume', "rsvDate"]
        widgets = {
		    'bloodType': TextInput(attrs={'size': 10, 'title': 'Blood Type'}),
            'rsvVolume': NumberInput(attrs={'title': 'reserved volume'}),
            'rsvDate': DateInput(format='%m/%d/%Y', attrs={'title': 'mm/dd/yyyy'})
        }
