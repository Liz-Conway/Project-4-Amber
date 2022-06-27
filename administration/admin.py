from django.contrib import admin
from .models import Diagnosis
from hippotherapy.models import Hat, Function, Skill, Hint
from administration.models import Horse, Task

# Register your models here.
# These models will appear and be modifiable in the Django Admin panel.
admin.site.register(Diagnosis)
admin.site.register(Hat)
admin.site.register(Horse)
admin.site.register(Task)
class TaskAdmin(admin.ModelAdmin):
    # Show if a task is mounted on the list of tasks
    list_display = ('task_name', 'mounted')
    search_fields = ('task_name')
    list_filter = ('mounted')
    
admin.site.register(Function)
admin.site.register(Skill)
admin.site.register(Hint)
