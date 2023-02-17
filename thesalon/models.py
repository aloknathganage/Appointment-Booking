from django.db import models
from django.db.models import Model


# Create your models here.
class Appoinments(models.Model):
    Name = models.CharField(max_length=50,null=True, blank=True)
    Age = models.IntegerField(null=True, blank=True)
    GENDER_MALE = 0
    GENDER_FEMALE = 1
    GENDER_CHOICES = [(GENDER_MALE, 'Male'), (GENDER_FEMALE, 'Female')]
    Gender = models.IntegerField(choices=GENDER_CHOICES)
    Phone = models.IntegerField(null=True, blank=True)
    DateTime = models.DateTimeField(default="2022-03-29 22:25" )
    Message = models.TextField(null=True, blank=True)
    def __str__(self):
        return self.Name


class Registerd(models.Model):
    # username = models.CharField(max_length=50,null=True, blank=True)
    email = models.EmailField(max_length = 100)
    name = models.CharField(max_length=50,null=True, blank=True)
    # lname = models.CharField(max_length=50,null=True, blank=True)
    password1 = models.CharField(max_length=50)
    password2 = models.CharField(max_length=50)
    def __str__(self):
        return self.name
