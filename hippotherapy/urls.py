"""amber hippotherapy URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')

"""

'''
Created on 14 Apr 2022

@author: liz
'''
from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomePage.as_view(), name='home'),
    path('addClient', views.AddClient.as_view(), name='addClient'),
    path('selectClient', views.SelectClient.as_view(), name='selectClient'),
    path('recordSession/<client>/', views.RecordSession.as_view(), name='recordSession'),
    path('observeSession/<session>/', views.ObserveSession.as_view(), name='observeSession'),
]
