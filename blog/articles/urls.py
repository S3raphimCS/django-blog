from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="home"),
    path('about', views.about, name="about"),
    path('contacts', views.contacts, name='contacts'),
    path('article-<int:pk>', views.ArticleDetailView.as_view(), name="article-view"),
    path('create', views.article_create, name='article_create'),
]