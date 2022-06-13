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
Created on 14 Jun 2022

@author: liz
'''
from django.urls import path
from . import views

urlpatterns = [
    path('addUser', views.AddUser.as_view(), name='addUser'),
    path('myAccount', views.MyAccount.as_view(), name='myAccount'),
]
