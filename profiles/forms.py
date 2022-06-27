from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from profiles.models import HippotherapyUser
from django.contrib.auth.models import User
from django import forms

# https://www.codeunderscored.com/django-roles-permissions-and-groups/
class HippotherapyUserCreationForm(UserCreationForm):
    """
    Form that allows the Admin to create users on the Amber application.
    """      
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
    """
    Form that allows the users to 
    change their own details on the Amber application.
    """      

    class Meta:
        model = HippotherapyUser
        fields = ('first_name', 'last_name')
        
        widgets = {
            'first_name': forms.TextInput(attrs={
                'class': 'formInput',
                'placeholder': 'First Name'
            }),
            'last_name': forms.TextInput(attrs={
                'class': 'formInput',
                'placeholder': 'Last Name'
            }),
        }
        
