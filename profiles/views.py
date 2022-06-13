from django.shortcuts import render
from profiles.forms import HippotherapyUserCreationForm
from django.views.generic.base import TemplateView
from django.contrib import messages


class AddUser(TemplateView):
    template_name = 'profiles/addUser.html'
    
    """
    In class-based views:
    Instead of using an if statement to check the request method,  
    we simply create class methods called GET, POST, or any other HTTP verb.
    """
    def get(self, request, *args, **kwargs):
        """
        '*args' = Standard arguments parameter
        '**kwargs' = Standard keyword arguments parameter
        """
        form = HippotherapyUserCreationForm()
        
        return render(
            request, 
            self.template_name, # view to render
            # Context - passed into the HTML template
            {
                "form": form, 
            }
        )
        
    """
    In class based views -
    GET & POST are supplied as class methods
    """
    def post(self, request, *args, **kwargs):
        """
        '*args' = Standard arguments parameter
        '**kwargs' = Standard keyword arguments parameter
        """
            
        """
        Get the data from our form
        and assign it to a variable.
        Gets all of the data that we posted from our form
        """
        add_user_form = HippotherapyUserCreationForm(data=request.POST)
        
        """
        Form is valid => If all the fields have been completed
        """
        if add_user_form.is_valid():
            add_user_form.save()
            first_name = request.POST['first_name']
            last_name = request.POST['last_name']
            messages.success(request,
                             f'New User <span class="name">{first_name} {last_name}</span> added successfully.',
                             extra_tags='safe')
        else:
            """
            If the form is NOT valid  
            then return an  empty 'add user' form instance
            showing the errors
            """
            messages.error(request, '<span class="boldEntry">Invalid form submission.</span>', extra_tags='safe')
            messages.error(request, add_user_form.errors)

        """
        Send all of this information to our render method
        """
        return render(
            request, 
            self.template_name, # View to render
            # Context - passed into the HTML template
            { 
                'form': HippotherapyUserCreationForm(),
            }
        )

