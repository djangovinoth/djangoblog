from django import forms
from django.contrib.auth.forms import User
from django.contrib.auth.forms import UserCreationForm
from .models import EmployeeEduDetailsModel
from django.urls import reverse
from crispy_forms.bootstrap import Field, InlineRadios, TabHolder, Tab
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Div, Fieldset
from django_countries.fields import CountryField
from django_countries.widgets import CountrySelectWidget
from django.forms import ModelForm, Textarea,TextInput,Select
from django.db.models import CharField


class EmployeeEduDetailsForm(forms.Form):

    QUALIFICATION= [
        ('10th', '10th'),
        ('12th', '12th'),
        ('intermidiate', 'intermidiate'),
        ('diploma', 'diploma'),
        ('UG', 'UG'),
        ('PG', 'PG'),
        ('Other', 'Other'),

        ]



    YEAR= [


        ]
    SPECILIZATION= [
        ('BE', 'BE'),
        ('ECE', 'ECE'),

        ]

    institutionname = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'name':'institutionname','class': "form-control",'placeholder': 'School name'}))
    specialization = forms.ChoiceField(choices=SPECILIZATION,widget=forms.Select(attrs={'name':'specialization','class':'form-control'}))
    yearofpassing = forms.ChoiceField(choices=[(x, x) for x in range(1900, 2020)],widget=forms.Select(attrs={'name':'yearofpassing','class':'form-control'}))
    score=forms.IntegerField(widget=forms.TextInput(attrs={'name':'score','class': "form-control",'placeholder': 'score'}))
    qualification = forms.ChoiceField(choices=QUALIFICATION,widget=forms.Select(attrs={'name':'qualification','class':'form-control'}))
