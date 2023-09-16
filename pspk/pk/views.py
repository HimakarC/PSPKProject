from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse, response
from django.contrib.auth.models import User, auth

# Create your views here.

def movies(request):
    return render(request, 'movies.html')

def songs(request):
    return render(request, 'songs.html')

def gallery(request):
    return render(request, 'gallery.html')

def speeches(request):
    return render(request, 'speeches.html')

def logout(request):
    auth.logout(request)
    return redirect('/')

def back(request):
    return redirect('/')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username = username, password = password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, "User doesn't exists")
            return redirect('register')
    else:
        return render(request, 'login.html')

def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password = request.POST['password']
        passwordcheck = request.POST['passwordcheck']
        if password == passwordcheck:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username is already exists')
                return render(request, 'register.html')
            else:
                user = User.objects.create_user(username=username, password=password, first_name=first_name, last_name=last_name)
                user.save()
                return redirect('login')
        else:
            messages.info(request, 'password is not correct')
            return render(request, 'register.html')
    else:
        return render(request, 'register.html')