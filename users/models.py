from django.db import models
from django.contrib.auth.models import AbstractUser ,BaseUserManager

# Create your models here.

class CustomUserManager(BaseUserManager):

    def create_user(self,email,password,**extra_fields):
        if not email:
            raise ValueError("Email must be set")
        
        email = self.normalize_email(email)
        user = self.model(email=email,**extra_fields)
        user.set_password(password)
        user.save()
        return user
    
    def create_superuser(self,email,password,**extra_fields):
        extra_fields.setdefault('is_staff',True)
        extra_fields.setdefault('is_superuser',True)
        extra_fields.setdefault('is_active',True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError("Superuser must be is_staff=True") 
        
        if extra_fields.get('is_superuser') is not True:
            raise ValueError("Superuser must be is_superuser=True")

        return self.create_user(email,password,**extra_fields)

    pass


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
    phone = models.CharField(max_length=20,unique=True,blank=True)
    email = models.EmailField(max_length=255,unique=True)
    user_type = models.CharField(max_length=10,choices=choices,default='1')

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def __str__(self):
        return self.email


