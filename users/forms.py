from django import forms
from django.contrib.auth.forms import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile,EdudetailsModel,PersonalDetailsModel,PermissionModel
from django.urls import reverse
from crispy_forms.bootstrap import Field, InlineRadios, TabHolder, Tab
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Div, Fieldset
from django_countries.fields import CountryField
from django_countries.widgets import CountrySelectWidget

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class PermissionForm(forms.ModelForm):

    class Meta:
        model = PermissionModel
        fields = ['phone', 'role','company','resume']



class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()


    class Meta:
        model = User
        fields = ['username', 'email']

class ProfileRegisterForm(forms.ModelForm):
    class Meta:
        model = Profile

        fields = ['phone','image','resume']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile

        fields = ['phone','image','resume']



class ProfilePhoneUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['phone']


class ProfileImageUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile

        fields = ['image']


class ProfileResumeUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile

        fields = ['resume']

class CompanyDetailsUpdateForm(forms.Form):
    companyname = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'name':'companyname','class': "form-control",'placeholder': 'Company name'}))
    exp = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'name':'exp','class': "form-control",'placeholder': 'exprience'}))

class SkillSetDetailsUpdateForm(forms.Form):
    skillname = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'name':'skillname','class': "form-control",'placeholder': 'Skill name'}))
    exp = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'name':'exp','class': "form-control",'placeholder': 'exprience'}))



class EduDetailsUpdateForm(forms.Form):

    schoolX = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'name':'schoolX','class': "form-control",'placeholder': 'School name'}))
    specializationX = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'name':'specializationX','class': "form-control",'placeholder': 'specialization'}))
    yearOfPassingX = forms.ChoiceField(choices=[(x, x) for x in range(1900, 2020)],widget=forms.Select(attrs={'name':'yearOfPassingX','class':'form-control'}))
    scoreX=forms.IntegerField(widget=forms.TextInput(attrs={'name':'scoreX','class': "form-control",'placeholder': 'percentage'}))

    schoolXII = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'name':'schoolXII','class': "form-control",'placeholder': 'High School name'}))
    specializationXII = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'name':'specializationXII','class': "form-control",'placeholder': 'specialization'}))
    yearOfPassingXII = forms.ChoiceField(choices=[(x, x) for x in range(1900, 2020)],widget=forms.Select(attrs={'name':'yearOfPassingXII','class':'form-control'}))
    scoreXII =forms.IntegerField(widget=forms.TextInput(attrs={'name':'scoreXII','class': "form-control",'placeholder': 'percentage'}))

    diploma = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'name':'diploma','class': "form-control",'placeholder': 'Dimploma college name'}))
    specializationDiploma = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'name':'specializationDiploma','class': "form-control",'placeholder': 'specialization'}))
    yearOfPassingDiploma = forms.ChoiceField(choices=[(x, x) for x in range(1900, 2020)],widget=forms.Select(attrs={'name':'yearOfPassingDiploma','class':'form-control'}))
    scoreDiploma=forms.IntegerField(widget=forms.TextInput(attrs={'name':'scoreDiploma','class': "form-control",'placeholder': 'percentage'}))

    UG = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'name':'UG','class': "form-control",'placeholder': 'UG College name'}))
    specializationUG = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'name':'specializationUG','class': "form-control",'placeholder': 'specialization'}))
    yearOfPassingUG = forms.ChoiceField(choices=[(x, x) for x in range(1900, 2020)],widget=forms.Select(attrs={'name':'yearOfPassingUG','class':'form-control'}))
    scoreUG=forms.IntegerField(widget=forms.TextInput(attrs={'name':'scoreUG','class': "form-control",'placeholder': 'percentage'}))

    PG = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'name':'PG','class': "form-control",'placeholder': 'PG College name'}))
    specializationPG = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'name':'specializationPG','class': "form-control",'placeholder': 'specialization'}))
    yearOfPassingPG = forms.ChoiceField(choices=[(x, x) for x in range(1900, 2020)],widget=forms.Select(attrs={'name':'yearOfPassingPG','class':'form-control'}))
    scorePG=forms.IntegerField(widget=forms.TextInput(attrs={'name':'scorePG','class': "form-control",'placeholder': 'percentage'}))


class PersonalDetailsUpdateForm(forms.Form):

    GENDER= [
        ('Male', 'M'),
        ('Female', 'F'),
        ('Other', 'O'),

        ]
    STATE= [
        ('Current Location', 'Current Location'),
        ('Tamil Nadu', 'Tamil Nadu'),
        ('Andra', 'Andra'),
        ('Kerala', 'Kerala'),
        ('Karnataka', 'Karnataka'),

        ]


    firstName = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'name':'firstName','class': "form-control",'placeholder': 'First Name'}))
    lastName = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'name':'lastName','class': "form-control",'placeholder': 'Last Name'}))
    fatherName = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'name':'fatherName','class': "form-control",'placeholder': 'Father Name'}))
    phoneNumber=forms.IntegerField(widget=forms.TextInput(attrs={'name':'phoneNumber','class': "form-control",'placeholder': 'Phone Number'}))
    gender = forms.CharField(label='Gender:',widget=forms.RadioSelect(attrs={'name':'gender','class':'form-control'},choices=GENDER))
    countryName = CountryField().formfield(widget=CountrySelectWidget(attrs={"name":"countryName","class": "form-control"}))
    dateOfBrith=forms.DateField(label='DOB:',widget=forms.TextInput(attrs={'id':'datepicker','class':'form-control','name':'dateOfBrith','class':'datepicker'}))
    currentLocation = forms.ChoiceField(label='Current Location:',choices=STATE,widget=forms.Select(attrs={'name':'currentLocation','class':'form-control'}))
    panNumber = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'name':'panNumber','class': "form-control",'placeholder': 'PAN Number'}))
    aatharNumber = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'name':'aatharNumber','class': "form-control",'placeholder': 'Aathar Number'}))
    currnetMailAddress = forms.CharField(max_length=100,widget=forms.Textarea(attrs={'name':'currnetMailAddress','class': "form-control",'placeholder': 'Currenet Mailing Address'}))
    permanentMailAddress = forms.CharField(max_length=100,widget=forms.Textarea(attrs={'name':'permanentMailAddress','class': "form-control",'placeholder': 'Permanent Mailing Address'}))
