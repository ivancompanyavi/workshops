from django.shortcuts import render_to_response
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.template import RequestContext
from django.http import HttpResponseRedirect
from .models import Worker, Workshop
from .forms import RegisterForm, LoginForm, AvatarForm, WorkshopModelForm


def home(request):
    return render_to_response('index.html', {}, RequestContext(request))


def workshops(request):
    workshops = Workshop.objects.all()
    return render_to_response('workshops.html', {'workshops': workshops}, RequestContext(request))


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
            new_user = authenticate(username=username, password=password)
            worker = Worker(user=new_user, team=team)
            worker.save()
            login(request, new_user)
            return HttpResponseRedirect('/')

    else:
        form = RegisterForm()
    return render_to_response('register.html', {'form': form}, RequestContext(request))


def profile(request):
    worker = Worker.objects.get(user__pk=request.user.pk)
    return render_to_response('profile.html', {'worker': worker}, RequestContext(request))


def change_avatar(request):
    worker = Worker.objects.get(user__pk=request.user.pk)
    form = AvatarForm(instance=worker)
    if request.method == 'POST':
        form = AvatarForm( request.POST, request.FILES, instance=worker)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/profile')
        else:
            print "avatar invalido"
    return render_to_response('change_avatar.html', {'form': form}, RequestContext(request))


def create_workshop(request):
    if request.method == 'POST':
        form = WorkshopModelForm(request.POST)
        if form.is_valid():
            workshop_model = form.save(commit=False)
            workshop_model.commiter = Worker.objects.get(user=request.user)
            workshop_model.save()
            return HttpResponseRedirect('/profile')
    else:
        form = WorkshopModelForm()
    return render_to_response('create_workshop.html', {'form': form}, RequestContext(request))


def workshop_detail(request, workshop_id):
    workshop = Workshop.objects.get(pk=workshop_id)
    return render_to_response('workshop_detail.html', {'workshop': workshop}, RequestContext(request))


def workshop_subscribe(request, workshop_id):
    workshop = Workshop.objects.get(pk=workshop_id)
    worker = Worker.objects.get(user=request.user)
    if workshop.commiter == worker:
        messages.add_message(request, messages.ERROR, 'You are the owner of that workshop. You cannot subscribe to it')
    else:
        worker.workshops_subscribed.add(workshop)
        messages.add_message(request, messages.INFO, 'You have been successfully subscribed to the workshop "%s"' % workshop.name)
    return HttpResponseRedirect('/workshops')