from django.db import models


class Diagnosis(models.Model):
    # null = False attribute here prevents Diagnoses from being created without a diagnosis field programmatically
    # and blank = False will make the field required on forms.
    diagnosis = models.CharField(max_length=32, null=False, blank=False)
    
    def __str__(self):
        return self.diagnosis
    
