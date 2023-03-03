from django.shortcuts import render, redirect
from .forms import UserLoginForm, UserRegistrationForm, UserProfileForm
from django.contrib import auth
from articles.models import Article


def login(request):
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
    if request.method == 'POST':
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
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
            return redirect('profile')
    else:
        form = UserProfileForm(instance=request.user)
    context = {'form': form, 'date_joined': request.user.date_joined, 'articles': Article.objects.all().filter(author=request.user)}
    print(context['articles'])
    return render(request, 'users/profile.html', context)
