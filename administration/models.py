from django.db import models


class Diagnosis(models.Model):
    # null = False attribute here prevents Diagnoses from being created without a diagnosis field programmatically
    # and blank = False will make the field required on forms.
    diagnosis = models.CharField(max_length=32, null=False, blank=False, unique=True)
    
    def __str__(self):
        return self.diagnosis


class Horse(models.Model):
    # null = False attribute here prevents Horse from being created without a horse_name field programmatically
    # and blank = False will make the field required on forms.
    horse_name = models.CharField(max_length=32, null=False, blank=False, unique=True)
    
    def __str__(self):
        return self.horse_name


class Task(models.Model):
    # null = False attribute here prevents Horse from being created without a horse_name field programmatically
    # and blank = False will make the field required on forms.
    task_name = models.CharField(max_length=40, null=False, blank=False, unique=True)
    mounted = models.BooleanField(default=False)
    
    def __str__(self):
        return self.task_name
