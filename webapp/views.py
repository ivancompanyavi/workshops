from django.shortcuts import render_to_response
from django.contrib.auth import authenticate, login as l


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

    return render_to_response('login.html', {})