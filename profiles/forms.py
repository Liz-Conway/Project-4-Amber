from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from profiles.models import HippotherapyUser
from django.contrib.auth.models import User
from django import forms


class HippotherapyUserCreationForm(UserCreationForm):
      
    class Meta:
        model = HippotherapyUser
        fields = ('username', 'first_name', 'last_name', 'role')
        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'formInput fadeInHelp',
                'placeholder': 'User Name'
            }),
            'first_name': forms.TextInput(attrs={
                'class': 'formInput',
                'placeholder': 'First Name'
            }),
            'last_name': forms.TextInput(attrs={
                'class': 'formInput',
                'placeholder': 'Last Name'
            }),
        }

class HippotherapyUserChangeForm(UserChangeForm):
    
    class Meta:
        model = HippotherapyUser
        fields = ('username', 'first_name', 'last_name', 'role')
        
        
