from django.db import models
from django.contrib.auth.models import AbstractUser

# https://learndjango.com/tutorials/django-custom-user-model
class HippotherapyUser(AbstractUser):
    ADMIN = 1
    OT = 2
    ANALYST =3

    ROLE_CHOICES = (
        (ADMIN, 'Administrator'),
        (OT, 'Occupational Therapist'),
        (ANALYST, 'Hippotherapy Analyst'),
    )
    role = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, blank=False, null=True)
    
    def user_role(self):
        return dict(HippotherapyUser.ROLE_CHOICES)[self.role]

