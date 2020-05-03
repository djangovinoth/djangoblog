from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from phone_field import PhoneField
from .validators import validate_file_extension
from django_countries.fields import CountryField
from django.contrib.auth.models import AbstractUser
from django.utils import timezone




class PermissionModel(models.Model):
    ROLE= [
        ('Employee', 'S'),
        ('Employer', 'E'),
        ]

    user=models.OneToOneField(User,on_delete=models.CASCADE)
    phone = models.IntegerField(blank=True, null=True)
    role=models.CharField(max_length=100,choices=ROLE)
    company=models.CharField(max_length=100)
    active=models.BooleanField(default=True)
    resume=models.FileField(upload_to="resume", validators=[validate_file_extension])
    image=models.ImageField(default='default.jpg',upload_to='profile_pics')


    def __str__(self):
        return self.user.username


    # def save(self, *args, **kwargs):
    #     super(PermissionModel, self).save(*args, **kwargs)
        # img=Image.open(self.image.path)
        #
        # if img.height>300 or img.width>300:
        #     output_size=(300,300)
        #     img.thumbnail(output_size)
        #     img.save(self.image.path)

class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    phone = models.IntegerField(blank=True, null=True)

    image=models.ImageField(default='default.jpg',upload_to='profile_pics')
    resume=models.FileField(upload_to="resume", validators=[validate_file_extension])


    def __str__(self):
        return f'{self.user.username} Profile'

    # def save(self):
    #     super().save()

    def save(self, *args, **kwargs):
        super(Profile, self).save(*args, **kwargs)
        img=Image.open(self.image.path)

        if img.height>300 or img.width>300:
            output_size=(300,300)
            img.thumbnail(output_size)
            img.save(self.image.path)



class EdudetailsModel(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    schoolX = models.CharField(blank=True, null=True,max_length=100)
    specializationX = models.CharField(blank=True, null=True,max_length=100)
    yearOfPassingX = models.IntegerField(blank=True, null=True)
    scoreX=models.IntegerField(blank=True, null=True)

    schoolXII = models.CharField(blank=True, null=True,max_length=100)
    specializationXII = models.CharField(blank=True, null=True,max_length=100)
    yearOfPassingXII = models.IntegerField(blank=True, null=True)
    scoreXII =models.IntegerField(blank=True, null=True)

    diploma = models.CharField(blank=True, null=True,max_length=100)
    specializationDiploma = models.CharField(blank=True, null=True,max_length=100)
    yearOfPassingDiploma = models.IntegerField(blank=True, null=True)
    scoreDiploma=models.IntegerField(blank=True, null=True)

    UG = models.CharField(blank=True, null=True,max_length=100)
    specializationUG = models.CharField(blank=True, null=True,max_length=100)
    yearOfPassingUG = models.IntegerField(blank=True, null=True)
    scoreUG=models.IntegerField(blank=True, null=True)

    PG = models.CharField(blank=True, null=True,max_length=100)
    specializationPG = models.CharField(blank=True, null=True,max_length=100)
    yearOfPassingPG = models.IntegerField(blank=True, null=True)
    scorePG=models.IntegerField(blank=True, null=True)

    # def save(self, *args, **kwargs):
    #     super(Profile, self).save(*args, **kwargs)






class PersonalDetailsModel(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,related_name='personaldetailsmodel')
    firstName = models.CharField(blank=True, null=True,max_length=100)
    lastName = models.CharField(blank=True, null=True,max_length=100)
    fatherName = models.CharField(blank=True, null=True,max_length=100)
    phoneNumber=models.IntegerField(blank=True, null=True)
    gender=models.CharField(blank=True, null=True,max_length=100)
    countryName=CountryField()
    dateOfBrith=models.CharField(blank=True, null=True,max_length=100)
    currentLocation=models.CharField(blank=True, null=True,max_length=100)
    panNumber = models.CharField(blank=True, null=True,max_length=100)
    aatharNumber = models.CharField(blank=True, null=True,max_length=100)
    currnetMailAddress = models.CharField(blank=True, null=True,max_length=100)
    permanentMailAddress = models.CharField(blank=True, null=True,max_length=100)

class CompanyDetailsModel(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='companydetailsmodel')
    companyname = models.CharField(blank=True, null=True,max_length=100)
    exp = models.CharField(blank=True, null=True,max_length=100)

class SkillSetDetailsModel(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='skillsetdetailsmodel')
    skillname = models.CharField(blank=True, null=True,max_length=100)
    exp = models.CharField(blank=True, null=True,max_length=100)
