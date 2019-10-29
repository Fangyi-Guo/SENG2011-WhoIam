from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Comment
from django.forms import ModelForm


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']
        help_texts = {
            'username': None,
            'email': None,
        }
        

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['body']

