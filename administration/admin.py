from django.contrib import admin
from .models import Diagnosis
from hippotherapy.models import Hat, Function, Skill, Hint
from administration.models import Horse, Task

# Register your models here.
admin.site.register(Diagnosis)
admin.site.register(Hat)
admin.site.register(Horse)
admin.site.register(Task)
admin.site.register(Function)
admin.site.register(Skill)
admin.site.register(Hint)
