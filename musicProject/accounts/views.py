from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from .models import *
# Create your views here.

def signup(request):
    if request.method == 'POST':
        # User has info and wants an account now!
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.get(username=request.POST['username'])
                return render(request, 'accounts/signup.html', {'error': 'Username has already been taken'})
            except User.DoesNotExist:
                user = User.objects.create_user(
                    username=request.POST['username'], password=request.POST['password1'])
                nickname = request.POST['nickname']
                profile_image = request.POST['profile_image']
                musicUser = MusicUser(user=user, nickname=nickname, profile_image=profile_image)
                musicUser.save()
                auth.login(request, user)
                return redirect('music:index')
        else:
            return render(request, 'accounts/signup.html', {'error': 'Passwords must match'})
    else:
        # User wants to enter info
        return render(request, 'accounts/signup.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)                
            return redirect('music:index')
        else:
            return render(request, 'accounts/login.html', {'error': 'username or password is incorrect.'})
    else:
        return render(request, 'accounts/login.html')

def logout(request):
    if request.method == "POST":
        auth.logout(request)
        return redirect('music:index')
    return render(request, 'accounts/make_new_account.html')
