from django.db import models
from administration.models import Diagnosis, Horse, Task


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
    diagnosis = models.ManyToManyField(Diagnosis, related_name="condition", blank=True)
    degree_of_difficulty = models.TextField(null=True, blank=True)
    additional_notes = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.first_name + " " + self.last_name
    

class Function(models.Model):
    function_name = models.CharField(max_length=32, null=False, blank=False, unique=True) 
    
    def __str__(self):
        return self.function_name
    
    
class Skill(models.Model):
    skill_name = models.CharField(max_length=32, null=False, blank=False, unique=True)
    function = models.ForeignKey(Function, related_name='functional_skill', on_delete=models.CASCADE)
    
    def __str__(self):
        return self.skill_name
    

class Hint(models.Model):
    hint_name = models.TextField(null=False, blank=False)    
    skill = models.ForeignKey(Skill, related_name='skill_hint', on_delete=models.CASCADE)
    order_in_skill = models.IntegerField(null=False, blank=False)
    
    class Meta:
        ordering = ['skill', 'order_in_skill']
    
    def __str__(self):
        return self.hint_name[0:16]
    
    
class Course(models.Model):
    id = models.AutoField(primary_key=True)
    client = models.ForeignKey(Client, related_name='participates', on_delete=models.CASCADE)
    
    def __str__(self):
        return str(self.id)
    
class Session(models.Model):
    course = models.ForeignKey(Course, related_name='courses', on_delete=models.CASCADE)
    week_number = models.IntegerField(null=False, blank=False)
    # Automatically adds the date when this object is first saved to database
    session_date = models.DateField()
    horse = models.ForeignKey(Horse, related_name='ridden', on_delete=models.PROTECT)
    tasks = models.ManyToManyField(Task, related_name='performed', blank=True)
    skill = models.ManyToManyField(through='SkillScore', to=Skill, related_name='skill_score')

    def __str__(self):
        return f"{self.course.id} / {self.week_number}"

# https://awbacker.io/migrating-an-existing-django-manytomany-to-a-through-model/
class SkillScore(models.Model):
    session = models.ForeignKey(Session, related_name='score_session', on_delete=models.PROTECT)
    skill = models.ForeignKey(Skill, related_name='score_skill', on_delete=models.PROTECT)
    score = models.IntegerField()
    
    def __str__(self):
        return f'Session:{self.session} has a score of  {self.score}  for skill:{self.skill}'

