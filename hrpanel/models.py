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


class CreateNewJobModel(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='createnewjobmodel')
    jobid = models.IntegerField(blank=True, null=True)
    jobtitle = models.CharField(blank=True, null=True,max_length=100)
    experience =models.CharField(blank=True, null=True,max_length=100)
    clientname=models.CharField(blank=True, null=True,max_length=100)
    companyname=models.CharField(blank=True, null=True,max_length=100)
    mandatoryskils=models.CharField(blank=True, null=True,max_length=100)
    designation=models.CharField(blank=True, null=True,max_length=100)
    expectednoticeperiod=models.CharField(blank=True, null=True,max_length=100)
    jobdescription=models.CharField(blank=True, null=True,max_length=100)
    domain=models.CharField(blank=True, null=True,max_length=100)
    joblocation=models.CharField(blank=True, null=True,max_length=100)
    contactname=models.CharField(blank=True, null=True,max_length=100)
    contactmailid=models.CharField(blank=True, null=True,max_length=100)
    contactmobilenumber=models.CharField(blank=True, null=True,max_length=100)
    payscalefromlacks=models.IntegerField(blank=True, null=True)
    payscalefromthousand=models.IntegerField(blank=True, null=True)
    payscaletolacks=models.IntegerField(blank=True, null=True)
    payscaletothousand=models.IntegerField(blank=True, null=True)
    contractjob=models.CharField(blank=True, null=True,max_length=100)
    contractfromyear=models.IntegerField(blank=True, null=True)
    contractfrommonth=models.IntegerField(blank=True, null=True)
    contracttoyear=models.IntegerField(blank=True, null=True)
    contracttomonth=models.IntegerField(blank=True, null=True)
