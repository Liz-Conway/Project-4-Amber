from django.shortcuts import render
from django.views.generic import TemplateView
from hippotherapy.forms import ClientForm
from django.template.defaultfilters import safe
from hippotherapy.models import Hat

# Create your views here.
class HomePage(TemplateView):
    template_name = "hippo/index.html"

class AddClient(TemplateView):
    template_name = "hippo/addClient.html"
    form_class = ClientForm
    
    
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
        form = self.form_class()
        print(form)
        print(form.data)
        # print(form.hat_size)
        hat_sizes = Hat.objects.all()
        
        return render(
            request, 
            self.template_name, # view to render
            # Context - passed into the HTML template
            {
                "form": form, 
                "hat_sizes": hat_sizes,
            }
        )
