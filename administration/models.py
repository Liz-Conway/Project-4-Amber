from django.db import models
from django.contrib.auth.models import AbstractUser


class Diagnosis(models.Model):
    """
    The model that maps a diagnosis object to a corresponding table on the DB
    """
    # null = False attribute here prevents Diagnoses from 
    # being created without a diagnosis field programmatically
    # and blank = False will make the field required on forms,
    # unique = True means that duplicates are not allowed
    diagnosis = models.CharField(max_length=32, null=True, blank=True, unique=True)
    
    def __str__(self):
        """
        A string representation of a Diagnosis object.
        """
        return self.diagnosis


class Horse(models.Model):
    """
    Class representing the horse that will be ridden during a 
    Hippotherapy treatment session.
    """
    # null = False attribute here prevents Horse from 
    # being created without a horse_name field programmatically
    # and blank = False will make the field required on forms.
    # unique = True means that duplicate Horese objects are not allowed
    horse_name = models.CharField(max_length=32, null=False, blank=False, unique=True)
    
    def __str__(self):
        """
        A string representation of a Horse object - in this case just its name
        """
        return self.horse_name


class Task(models.Model):
    """
    Class representing the activities that a client will perform
    during a Hippotherapy treatment session.
    """
    # null = True attribute here since only some Tasks 
    # will be chosen for a given Session
    # and blank = True will allow for 
    # some Tasks not to be selected on forms.
    task_name = models.CharField(max_length=40, null=True, blank=True)
    # Whether the task was performed whilst on horse-back
    mounted = models.BooleanField(default=False)
    
    def __str__(self):
        """
        A string representation of a Task object.
        The name of the task + whether it is performed mounted.
        """
        task_str = self.task_name
        if(self.mounted):
            task_str = task_str + " (mounted)"
        return task_str
    
