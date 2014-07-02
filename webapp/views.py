from django.shortcuts import render_to_response
from django.contrib.auth import authenticate, login as l
from django.contrib.auth.models import User
from django.template import RequestContext
from django.http import HttpResponseRedirect
from .models import Worker
from .forms import RegisterForm


def home(request):
    return render_to_response('index.html', {})


def workshops(request):
    return render_to_response('workshops.html', {})


def login(request):
    if request.method == 'POST':
        form = request.POST
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']

        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                l(request, user)

    return render_to_response('login.html', {}, RequestContext(request))


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            email = form.cleaned_data['email']
            team = form.cleaned_data['team']
            user = User.objects.create_user(username=username, password=password, email=email)
            user.save()
            worker = Worker(user=user, team=team)
            worker.save()
            return HttpResponseRedirect('/home')

    else:
        form = RegisterForm()
    return render_to_response('register.html', {'form': form}, RequestContext(request))