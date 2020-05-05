from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from phone_field import PhoneField
from django_countries.fields import CountryField
from django.contrib.auth.models import AbstractUser
from django.utils import timezone

# Create your models here.

class ShortlistedCandiateModel(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='shortlistedcandiatemodel')
    candiatename = models.CharField(blank=True, null=True,max_length=100)
    jobid = models.CharField(blank=True, null=True,max_length=100)
    createddate=models.CharField(blank=True, null=True,max_length=100)
    updateddate=models.CharField(blank=True, null=True,max_length=100)
