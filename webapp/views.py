from django.shortcuts import render_to_response
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.template import RequestContext
from django.http import HttpResponseRedirect
from .models import Worker
from .forms import RegisterForm, LoginForm, AvatarForm


def home(request):
    return render_to_response('index.html', {}, RequestContext(request))


def workshops(request):
    return render_to_response('workshops.html', {}, RequestContext(request))


def make_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect('/')
            else:
                messages.add_message(request, messages.ERROR, 'The user you introduced is not valid')
    else:
        form = LoginForm()

    return render_to_response('login.html', {'form': form}, RequestContext(request))


def make_logout(request):
    logout(request)
    return render_to_response('index.html', {}, RequestContext(request))


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
            login(request, user)
            return HttpResponseRedirect('/')

    else:
        form = RegisterForm()
    return render_to_response('register.html', {'form': form}, RequestContext(request))


def profile(request):
    worker = Worker.objects.get(user__id=request.user.id)
    return render_to_response('profile.html', {'worker': worker}, RequestContext(request))

def change_avatar(request):
    worker = Worker.objects.get(user__id=request.user.id)
    form = AvatarForm(instance=worker)
    if request.method == 'POST':
        form = AvatarForm( request.POST, request.FILES, instance=worker)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/profile')
        else:
            print "avatar invalido"
    return render_to_response('change_avatar.html', {'form': form}, RequestContext(request))