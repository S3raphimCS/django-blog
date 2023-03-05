from django.shortcuts import render, redirect
from .forms import UserLoginForm, UserRegistrationForm, UserProfileForm
from django.contrib import auth, messages
from articles.models import Article
from django.views.generic import DetailView
from .models import User

# TODO
# Need to do ProfileView for an pages with unique id for example "users/profiles/2021331" instead of "profile" func
# Because it needs access for any users to any user pages
# Button "Admin Panel" for superusers or staff
# Button "Create article"
# Better decor for "Последняя статья" in profile
# Views and rating in future
# form.errors in signup template (HINT - position: relative for independent blocks)
# Realize search in header
# Model for article on moderating and add to profile template user's articles on moderating
# Add permission for staff to moderate articles and post it on site


def login(request):
    if request.user.is_authenticated:
        return redirect('profile')
    if request.method == "POST":
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                return redirect('home')

    else:
        form = UserLoginForm()
    context = {'form': form}
    return render(request, 'users/login.html', context)


def sign_up(request):
    if request.user.is_authenticated:
        return redirect('profile')
    if request.method == 'POST':
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Вы были успешно зарегистрированы!')
            return redirect('login')
    else:
        form = UserRegistrationForm()
    context = {'form': form}
    return render(request, 'users/signup.html', context)


def profile(request):
    if request.method == 'POST':
        form = UserProfileForm(instance=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Данные профиля успешно изменены.')
            return redirect('profile')
    else:
        form = UserProfileForm(instance=request.user)
    context = {
        'form': form,
        'date_joined': request.user.date_joined,
        'articles': Article.objects.all().filter(author=request.user),
        'last_article': Article.objects.all().last()
               }
    return render(request, 'users/profile.html', context)
