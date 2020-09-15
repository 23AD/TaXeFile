from django.contrib import admin
from django.urls import path

from login1 import views

urlpatterns = [
    path('login1', views.login1, name='login1 page'),
]
