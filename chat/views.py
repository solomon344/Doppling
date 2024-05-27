from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages

# Create your views here.
# creating views here

def sign_up(request) :
    if request.method == 'POST' :
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been created successfully.')
            return redirect('login')
        
    else :
        form = UserCreationForm()
    return render(request, {'form', form})

def log_in(request) :
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
        
    else:
        form = AuthenticationForm()
    return render(request, {'form': form})


def log_out(request) :
    if request.method == 'POST':
        logout(request)
        return redirect('login')