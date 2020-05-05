from django import forms
from django.contrib.auth.forms import User
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse
from crispy_forms.bootstrap import Field, InlineRadios, TabHolder, Tab
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Div, Fieldset
from django_countries.fields import CountryField
from django_countries.widgets import CountrySelectWidget

class ShortlistedCandidateDetailsForm(forms.Form):
    candiatename = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'name':'candiatename','class': "form-control",'placeholder': 'Company name'}))
    
    jobid = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'name':'jobid','class': "form-control",'placeholder': 'exprience'}))
