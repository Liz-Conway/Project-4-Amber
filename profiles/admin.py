from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from profiles.forms import HippotherapyUserCreationForm,\
    HippotherapyUserChangeForm
from profiles.models import HippotherapyUser

class HippotherapyUserAdmin(UserAdmin):
    add_form = HippotherapyUserCreationForm
    form = HippotherapyUserChangeForm
    model = HippotherapyUser
    list_display = ['username', 'role', 'first_name', 'last_name']
    
admin.site.register(HippotherapyUser, HippotherapyUserAdmin)
