from django.urls import path
from . import views
from django.contrib.auth import views as authViews

# app_name = 'users'

urlpatterns = [
    path('login', views.login, name='login'),
    path('signup', views.sign_up, name='signup'),
    path('profile', views.profile, name='profile'),
    path('logout', authViews.LogoutView.as_view(next_page='home'), name='logout'),
]
