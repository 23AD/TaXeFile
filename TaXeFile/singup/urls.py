from django.contrib import admin
from django.urls import path

from singup import views

urlpatterns = [
    path('singup', views.singup, name='singup page'),
]