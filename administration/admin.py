from django.contrib import admin
from .models import Diagnosis
from hippotherapy.models import Hat

# Register your models here.
admin.site.register(Diagnosis)
admin.site.register(Hat)
