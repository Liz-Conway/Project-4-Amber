'''
Created on 20 Mar 2022

@author: fintan
'''
from django import forms
from administration.models import Diagnosis
import datetime
from django.db.models.fields import CharField
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
class DiagnosisForm(forms.ModelForm):
    """
    To tell the form which model it's going to be associated with,
    we need to provide an inner class called meta.
    This inner class just gives our form some information about itself.
    Like which fields it should render, how it should display error messages, and so on.
    """
    class Meta:
        model = Diagnosis
        """
        Define the fields to display explicitly in the inner metaclass on the item form.
        The reason for this is otherwise the form will display all fields on the model
        including those we might not want the user to see.
        """
        fields = ["diagnosis"]
        
        widgets={
                   "diagnosis":forms.TextInput(attrs={'class':'formInput', 'placeholder': 'New Diagnosis'}),
                }
        
        
