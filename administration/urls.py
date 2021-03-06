"""
amber administration URL Configuration

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
from . import views, validators

urlpatterns = [
    path('addDiagnosis/', views.DiagnosisList.as_view(), name='addDiagnosis'),
    path('addDiagnosis/validateDiagnosis', 
         validators.DiagnosisValidator.as_view(), name = "validateDiagnosis"),
]
