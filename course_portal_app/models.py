from random import choices
import re
from django import forms
from django.db import models
from django.db.models.fields import DateTimeField
from django.conf import settings
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin,AbstractUser
from django.db import models
from django.utils import timezone
from course_portal_app.managers import CustomUserManager

#do not touch this part
class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(('Email Address'), unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    class Meta():
        db_table = "Users"

    def __str__(self):
        return self.email


occupation_choices = (("Working","Working"), ("Student","Student"), ("Prefer Not to Say","Prefer Not to Say"))

class AccountDetails(models.Model):
    email = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    dob = models.DateField()
    mobile = models.IntegerField()
    occupation_status = models.CharField(max_length=20, choices=occupation_choices)
    college_name = models.CharField(max_length=50)
    course_name = models.CharField(max_length=30)

    class Meta():
        db_table = "account_details"
    
    

# class CustomUser(AbstractBaseUser, PermissionsMixin):
    
#     id = models.CharField("ID", max_length=10, primary_key=True)
#     email = models.EmailField('Email Address', unique=True, primary_key=True)
#     date_joined = models.DateTimeField(default=timezone.now)

#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = ['id','name']

#     objects = CustomUserManager()

#     class Meta():
#         db_table = "Users"

#     def __str__(self):
#         return self.email



