from django.shortcuts import render
from .forms import UserLoginForm


def login(request):
    context = {'form': UserLoginForm()}
    return render(request, 'users/login.html', context)


def sign_up(request):
    return render(request, 'users/signup.html')
