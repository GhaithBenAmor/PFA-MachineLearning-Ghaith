"""
        Important: this file is by default on project folder
        I copy this py file to app folder
"""
from django.urls import path, include
from . import views
from Home import views

urlpatterns = [

    path('', views.Home, name="home"),

]
