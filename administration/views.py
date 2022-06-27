from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from django.core import serializers
from django.http import JsonResponse
from .models import Diagnosis
from .forms import DiagnosisForm
from django.views import View
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

# https://www.pluralsight.com/guides/work-with-ajax-django
# How to add an item on the same page that display an existing list of "stuff"
class DiagnosisList(LoginRequiredMixin, UserPassesTestMixin, View):
    """
    A list of diagnoses that the Admin user will maintain.
    This class uses AJAX to redisplay the list after 
    the Admin user has added a new diagnosis.
    This means that the application will not make a round-trip to the server
    and load another page.
    It will use AJAX and JSON to insert the newly
    added diagnosis to the existing list. 
    """
    form_class = DiagnosisForm
    template_name = 'admins/addDiagnosis.html'

    # In class-based views:
    # Instead of using an if statement to check the request method,  
    # we simply create class methods called GET, POST, or any other HTTP verb.
    def get(self, request, *args, **kwargs):
        """
        Uses the HTTP GET protocol to retrieve and display the initial
        list of diagnoses
        """
        # '*args' = Standard arguments parameter
        # '**kwargs' = Standard keyword arguments parameter
        form = self.form_class()
        
        # Retrieve all the diagnoses from the database
        diagnoses = Diagnosis.objects.all()

        # Send all the diagnoses to our render method
        return render(
            request, 
            self.template_name, # view to render
            # Context - passed into the HTML template
            {
                'form': form, 
                'diagnoses': diagnoses
            }
        )

    # In class based views -
    # GET & POST are supplied as class methods
    def post(self, request, *args, **kwargs):
        """
        Uses the HTTP POST protocol to add a new diagnosis to the database
        """
        # '*args' = Standard arguments parameter
        # '**kwargs' = Standard keyword arguments parameter
        if request.method == "POST":
            # Get the data from our form and assign it to a variable.
            # Gets all of the data that we posted from our form
            form = self.form_class(request.POST)
            
            # Form is valid => If all the required fields have been completed
            if form.is_valid():
                instance = form.save()
                # Serialise the form data in JSON format
                ser_instance = serializers.serialize('json', [ instance, ])
                # send to client side.
                return JsonResponse({'instance': ser_instance}, status=200)
            else:
                # Set an invalid message
                messages.error(request, 'That diagnosis already exists')
                # Send a JSON error to the client
                return JsonResponse({'error': form.errors}, status=400)

        # Not post => Send an error to the client
        messages.error(request, 'Form not Posted correctly')
        return JsonResponse({'error': ''}, status=400)

    def test_func(self):
        """
        Only users with the ADMIN role can use this class
        """
        return self.request.user.user_role() == 'Administrator'
