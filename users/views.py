from django.shortcuts import render, redirect
from django.contrib import messages


def register(request):
    if request.method == 'POST':
        messages.error(request, 'wrong inputs')
        redirect('register')
    return render(request, 'users/register.html')


def login(request):
    return render(request, 'users/login.html')


def logout(request):
    return redirect('index')


def dashboard(request):
    return render(request, 'users/dashboard.html')
