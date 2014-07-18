
from django import forms
from django.contrib.auth.models import User
from django.db.models import Q

from core.models import Worker


class RegisterForm(forms.Form):

    username = forms.CharField(label='', required=True, widget=forms.TextInput(attrs={'placeholder': 'username'}))
    password = forms.CharField(label='', required=True,widget=forms.PasswordInput(attrs={'placeholder': 'password'}))
    email = forms.EmailField(label='', required=True, widget=forms.TextInput(attrs={'placeholder': 'email'}))
    team = forms.ChoiceField(label='', required=True, choices=Worker.TEAM_CHOICES, widget=forms.Select())

    def clean(self):
        username = self.cleaned_data['username']
        email = self.cleaned_data['email']

        if User.objects.filter(Q(username=username) | Q(email=email)).count():
            raise forms.ValidationError('The user or email you introduced is already registered in our database')
        return self.cleaned_data


class LoginForm(forms.Form):
    username = forms.CharField(label='', required=True, widget=forms.TextInput(attrs={'placeholder': 'username'}))
    password = forms.CharField(label='', required=True, widget=forms.PasswordInput(attrs={'placeholder': 'password'}))


class AvatarForm(forms.ModelForm):
    class Meta:
        model = Worker
        fields = ['avatar']