"""
        Important: this file is by default on project folder
        I copy this py file to app folder
"""
from django.urls import path, include
from . import views
from Visualization import views

urlpatterns = [

    path('Dashboard/', views.indexPage, name="Dashboard"),

]
