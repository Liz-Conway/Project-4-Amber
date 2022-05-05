from django.db import models
from administration.models import Diagnosis


class Hat(models.Model):
    # null = False attribute here prevents Hat from being created without a size field programmatically
    # and blank = False will make the field required on forms.
    size = models.CharField(max_length=32, null=False, blank=False, unique=True)
    
    class Meta:
        ordering = ['size']
    
    def __str__(self):
        return self.size
    
class Client(models.Model):
    first_name = models.CharField(max_length=32, null=False, blank=False)
    last_name = models.CharField(max_length=32, null=False, blank=False)
    SEX = [('M', 'Male'), ('F', 'Female')]
    gender = models.CharField(max_length=1, choices=SEX, null=False, blank=False, default='M')
    date_of_birth = models.DateField()
    hat_size = models.ForeignKey(Hat, related_name='wears', on_delete=models.PROTECT)
    diagnosis = models.ManyToManyField(Diagnosis, related_name="condition")
    degree_of_difficulty = models.TextField(null=True, blank=True)
    additional_notes = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.first_name + " " + self.last_name
    
    
