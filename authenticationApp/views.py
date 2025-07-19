from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required

from .forms import UserCreation

def registerPage(request):
    if request.user.is_authenticated:
        return redirect('/')
    else:
        if request.method == "POST":
            form = UserCreation(request.POST or None)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, "Accounted created for " + user)
                return redirect("login")
        else:
            form = UserCreation()
            
        return render(request, 'register.html', {'form': form})

def loginPage(request):
    if request.user.is_authenticated:
        return redirect('/')
    else:
        form = AuthenticationForm()

        if request.method == "POST":
            username = request.POST.get('username')
            password = request.POST.get('password')
            
            user = authenticate(request, username=username, password=password)
            
            if user is not None :
                login(request, user)
                return redirect("profile")
            else:
                messages.info(request, 'Username OR password is incorrect')
                return render(request, 'login.html', {'form': form})
            
        return render(request, 'login.html', {'form': form})
        #return render(request, 'login.html')

def logoutUser(request):
    logout(request)
    return redirect('login')

