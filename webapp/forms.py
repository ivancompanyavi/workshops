__author__ = 'ivancompany'

from django import forms
from .models import Worker

class RegisterForm(forms.Form):
    CLASS_ATTR = {'class': 'form-control'}

    username = forms.CharField(label='Username', required=True, widget=forms.TextInput(attrs=CLASS_ATTR))
    password = forms.CharField(label='Password', required=True,widget=forms.PasswordInput(attrs=CLASS_ATTR))
    email = forms.EmailField(label='Email', required=True, widget=forms.TextInput(attrs=CLASS_ATTR))
    team = forms.ChoiceField(label='Team', required=True, choices=Worker.TEAM_CHOICES, widget=forms.Select(attrs=CLASS_ATTR))
