from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    choices = (
        ('0','Teacher'),
        ('1','Student'),
        ('2','Company/Organisation/School/Institute'),
    )

    username=None
    first_name = None
    last_name = None
    name = models.CharField(max_length=100,blank=True)
    phone_number = models.CharField(max_length=20,unique=True,blank=True)
    email = models.EmailField(max_length=255,unique=True)
    user_type = models.CharField(max_length=10,choices=choices,default='1')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def __str__(self):
        return self.email


