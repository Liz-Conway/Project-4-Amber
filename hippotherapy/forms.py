'''
Created on 2 May 2022

@author: liz
'''
from django import forms
from administration.models import Diagnosis, Task
from hippotherapy.models import Client, Hat, Session
import datetime
from django.db.models.fields import CharField
from django.contrib.admin.utils import help_text_for_field
"""
Creating forms manually leaves our application open to errors if we don't validate them properly.
For example if we create a form and forget to mark one of the fields as required,
but that field is required on the database model -
Django would try to create an item
in our database with the missing field which could result in an error on the front-end
To alleviate this issue, in Django it's possible to create forms directly from the model itself.
And allow Django to handle all the form validation.
"""

"""
Our form will be a class that inherits a built-in Django class to give it some basic functionality.
"""

"""
The idea of creating this form in Django is that rather than writing an
entire form ourselves in HTML.
We can simply render it out as a template variable.
"""
class ClientForm(forms.ModelForm):
    """
    To tell the form which model it's going to be associated with,
    we need to provide an inner class called meta.
    This inner class just gives our form some information about itself.
    Like which fields it should render, how it should display error messages, and so on.
    """
    class Meta:
        model = Client
        """
        Define the fields to display explicitly in the inner metaclass on the item form.
        The reason for this is otherwise the form will display all fields on the model
        including those we might not want the user to see.
        """
        fields = ["first_name", "last_name", "gender", "date_of_birth", "hat_size", "diagnosis", "degree_of_difficulty", "additional_notes"]
        
        diagnosis = forms.ModelMultipleChoiceField(
                queryset=Diagnosis.objects.all(),
                 widget=forms.CheckboxSelectMultiple
            )
        
        widgets={
                   "first_name":forms.TextInput(attrs={'class':'formInput', 'placeholder': 'First name'}),
                   "last_name":forms.TextInput(attrs={'class':'formInput', 'placeholder': 'Surname'}),
                   "date_of_birth":forms.TextInput(attrs={'class':'dateInput formInput', 'placeholder': 'Date of Birth'}),
                   "gender":forms.RadioSelect(),
                   # "hat_size":forms.Select(attrs={'class':'dateInput'}
                            # queryset=Hat.objects.all().order_by('size')
                       # ),
                   "degree_of_difficulty":forms.Textarea(attrs={'class':'formInput', 'placeholder': 'Degree of Difficulty'}),
                   "additional_notes":forms.Textarea(attrs={'class':'formInput', 'placeholder': 'Enter any additional notes here'}),
                }
        
class SessionForm(forms.ModelForm):
    """
    To tell the form which model it's going to be associated with,
    we need to provide an inner class called meta.
    This inner class just gives our form some information about itself.
    Like which fields it should render, how it should display error messages, and so on.
    """
    class Meta:
        model = Session
        """
        Define the fields to display explicitly in the inner metaclass on the item form.
        The reason for this is otherwise the form will display all fields on the model
        including those we might not want the user to see.
        """
        fields = ["horse", "tasks", "course", "week_number", "session_date"]
        
        # tasks_unmounted = forms.ModelMultipleChoiceField(
        #         queryset=Task.objects.filter(mounted=False),
        #          widget=forms.CheckboxInput(attrs={'class': 'formInput'}),
        #     )
        #
        # tasks_mounted = forms.ModelMultipleChoiceField(
        #         queryset=Task.objects.filter(mounted=True),
        #          widget=forms.CheckboxInput(attrs={'class': 'formInput'}),
        #     )
        

        # tasks = forms.ModelMultipleChoiceField(
        #     queryset=Task.objects.all(),
        #     # widget=forms.CheckboxInput(attrs={'class': 'formInput'}),
        # )
        
        course = forms.IntegerField(widget=forms.HiddenInput())
        
        week_number = forms.IntegerField(widget=forms.HiddenInput())
        
        session_date = forms.DateField(widget=forms.HiddenInput())
        
        widgets={
                   "horse":forms.Select(),
                }
        
        
class ObservationForm(forms.ModelForm):
    session = forms.IntegerField(widget=forms.HiddenInput())
    
    """
    To tell the form which model it's going to be associated with,
    we need to provide an inner class called meta.
    This inner class just gives our form some information about itself.
    Like which fields it should render, how it should display error messages, and so on.
    """
    class Meta:
        # model = Client
        """
        Define the fields to display explicitly in the inner metaclass on the item form.
        The reason for this is otherwise the form will display all fields on the model
        including those we might not want the user to see.
        """
        # fields = ["first_name", "last_name"]    

