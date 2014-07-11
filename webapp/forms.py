__author__ = 'ivancompany'

from django import forms
from .models import Worker, Workshop, Question
from django.contrib.auth.models import User
from django.db.models import Q
from django.forms import TextInput, Textarea


class RegisterForm(forms.Form):
    CLASS_ATTR = {'class': 'form-control'}

    username = forms.CharField(label='Username', required=True, widget=forms.TextInput(attrs=CLASS_ATTR))
    password = forms.CharField(label='Password', required=True,widget=forms.PasswordInput(attrs=CLASS_ATTR))
    email = forms.EmailField(label='Email', required=True, widget=forms.TextInput(attrs=CLASS_ATTR))
    team = forms.ChoiceField(label='Team', required=True, choices=Worker.TEAM_CHOICES, widget=forms.Select(attrs=CLASS_ATTR))

    def clean(self):
        username = self.cleaned_data['username']
        email = self.cleaned_data['email']

        if User.objects.filter(Q(username=username) | Q(email=email)).count():
            raise forms.ValidationError('The user or email you introduced is already registered in our database')
        return self.cleaned_data


class LoginForm(forms.Form):
    CLASS_ATTR = {'class': 'form-control'}
    username = forms.CharField(label='Username', required=True, widget=forms.TextInput(attrs=CLASS_ATTR))
    password = forms.CharField(label='Password', required=True,widget=forms.PasswordInput(attrs=CLASS_ATTR))


class AvatarForm(forms.ModelForm):
    class Meta:
        model = Worker
        fields = ['avatar']


class WorkshopModelForm(forms.ModelForm):
    class Meta:
        CLASS_ATTR = {'class': 'form-control'}
        model = Workshop
        fields = ['name', 'description', 'prerequisites', 'objectives']
        widgets = {
            'name': TextInput(attrs=CLASS_ATTR),
            'description': Textarea(attrs=CLASS_ATTR),
            'prerequisites': Textarea(attrs=CLASS_ATTR),
            'objectives': Textarea(attrs=CLASS_ATTR),
        }

class QuestionModelForm(forms.ModelForm):
    class Meta:
        CLASS_ATTR = {'class': 'form-control'}
        model = Question
        fields = ['description', 'options']
        widgets = {
            'description': Textarea(attrs=CLASS_ATTR),
            }