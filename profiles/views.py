from django.shortcuts import render
from profiles.forms import HippotherapyUserCreationForm,\
    HippotherapyUserChangeForm
from django.views.generic.base import TemplateView
from django.contrib import messages
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


class AddUser(LoginRequiredMixin, UserPassesTestMixin, TemplateView):
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

    def test_func(self):
        return self.request.user.user_role() == 'Administrator'


class MyAccount(TemplateView):
    template_name = 'profiles/editUser.html'
    
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
        me = request.user
        print(f"I am ::  {me}")
        if me.is_anonymous:
            messages.warning(request, 'User is not logged in.  Please use the menu to log in.')
            return render(
                request,
                'index.html',
                {}
            )
        form = HippotherapyUserChangeForm(instance=me)
        username = me.username
        
        return render(
            request, 
            self.template_name, # view to render
            # Context - passed into the HTML template
            {
                'form': form,
                'username': username,
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
        user = request.user
        my_account_form = HippotherapyUserChangeForm(data=request.POST, instance=user)
        
        """
        Form is valid => If all the fields have been completed
        """
        if my_account_form.is_valid():
            my_account_form.save()
            messages.success(request,
                             f'You updated your account details successfully.',
                             extra_tags='safe')
        else:
            """
            If the form is NOT valid  
            then return an  empty 'add user' form instance
            showing the errors
            """
            messages.error(request, '<span class="boldEntry">Invalid form submission.</span>', extra_tags='safe')
            messages.error(request, my_account_form.errors)

        """
        Send all of this information to our render method
        """
        return render(
            request, 
            self.template_name, # View to render
            # Context - passed into the HTML template
            { 
                'form': HippotherapyUserChangeForm(instance=user),
            }
        )
