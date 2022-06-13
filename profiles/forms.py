from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from profiles.models import HippotherapyUser
from django.contrib.auth.models import User
from django import forms


class HippotherapyUserCreationForm(UserCreationForm):
      
    class Meta:
        model = HippotherapyUser
        fields = ('username', 'first_name', 'last_name', 'role')

class HippotherapyUserChangeForm(UserChangeForm):
    
    class Meta:
        model = HippotherapyUser
        fields = ('username', 'first_name', 'last_name', 'role')