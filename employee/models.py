from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from phone_field import PhoneField
from django_countries.fields import CountryField
from django.contrib.auth.models import AbstractUser
from django.utils import timezone

# Create your models here.
class EmployeeEduDetailsModel(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='employeeedudetailsmodel')
    institutionname = models.CharField(blank=True, null=True,max_length=100)
    specialization = models.CharField(blank=True, null=True,max_length=100)
    yearofpassing  = models.IntegerField(blank=True, null=True)
    score= models.CharField(blank=True, null=True,max_length=100)
    qualification= models.CharField(blank=True, null=True,max_length=100)
