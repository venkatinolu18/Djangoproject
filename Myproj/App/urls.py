from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='Home'),
    path('home/', views.home, name='home'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('<path:pagename>/', views.pagenotfound, name='pagenotfound'),
]