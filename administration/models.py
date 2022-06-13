from django.db import models
from django.contrib.auth.models import AbstractUser


class Diagnosis(models.Model):
    # null = False attribute here prevents Diagnoses from being created without a diagnosis field programmatically
    # and blank = False will make the field required on forms.
    diagnosis = models.CharField(max_length=32, null=True, blank=True)
    
    def __str__(self):
        return self.diagnosis


class Horse(models.Model):
    # null = False attribute here prevents Horse from being created without a horse_name field programmatically
    # and blank = False will make the field required on forms.
    horse_name = models.CharField(max_length=32, null=False, blank=False, unique=True)
    
    def __str__(self):
        return self.horse_name


class Task(models.Model):
    # null = True attribute here since only some Tasks will be chosen for a given Session
    # and blank = True will allow for some Tasks not to be selected on forms.
    task_name = models.CharField(max_length=40, null=True, blank=True)
    mounted = models.BooleanField(default=False)
    
    def __str__(self):
        task_str = self.task_name
        if(self.mounted):
            task_str = task_str + " (mounted)"
        return task_str
    
