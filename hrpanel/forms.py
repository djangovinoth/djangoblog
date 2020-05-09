from django import forms
from django.contrib.auth.forms import User
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse
from crispy_forms.bootstrap import Field, InlineRadios, TabHolder, Tab
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Div, Fieldset
from django_countries.fields import CountryField
from django_countries.widgets import CountrySelectWidget
from .models import CreateNewJobModel

class OfflineCandiateForm(forms.Form):
    offlinecandiate = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'name':'offlinecandiate','class': "form-control",'placeholder': 'offlinecandiate'}))
    uploadresume = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'name':'uploadresume','class': "form-control",'placeholder': 'uploadresume'}))
    phonenumber = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'name':'phonenumber','class': "form-control",'placeholder': 'phonenumber'}))
    candiateemailid = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'name':'candiateemailid','class': "form-control",'placeholder': 'candiateemailid'}))


class TechnicalTeamForm(forms.Form):
    empname = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'name':'empname','class': "form-control",'placeholder': 'empname'}))
    phonenumber = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'name':'phonenumber','class': "form-control",'placeholder': 'phonenumber'}))
    empid = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'name':'empid','class': "form-control",'placeholder': 'empid'}))
    currentdesignation = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'name':'currentdesignation','class': "form-control",'placeholder': 'currentdesignation'}))



class ShortlistedCandidateDetailsForm(forms.Form):

    candiatename = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'name':'candiatename','class': "form-control",'placeholder': 'Company name'}))

    jobid = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'name':'jobid','class': "form-control",'placeholder': 'exprience'}))




class CreateNewJobForm(forms.Form):
    jobid = forms.IntegerField(label="Job Id :",widget=forms.TextInput(attrs={'name':'jobid','id':'jobid','class': "form-control",'placeholder': 'jobid'}))
    jobtitle = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'name':'jobtitle','class': "form-control",'placeholder': 'jobtitle name'}))
    experience =forms.CharField(max_length=100,widget=forms.TextInput(attrs={'name':'experience','class': "form-control",'placeholder': 'experience'}))
    clientname=forms.CharField(max_length=100,widget=forms.TextInput(attrs={'name':'clientname','class': "form-control",'placeholder': 'clientname'}))
    companyname=forms.CharField(max_length=100,widget=forms.TextInput(attrs={'name':'companyname','class': "form-control",'placeholder': 'companyname'}))
    mandatoryskils=forms.CharField(max_length=100,widget=forms.TextInput(attrs={'name':'mandatoryskils','class': "form-control",'placeholder': 'mandatoryskils'}))
    designation=forms.CharField(max_length=100,widget=forms.TextInput(attrs={'name':'designation','class': "form-control",'placeholder': 'designation'}))
    expectednoticeperiod=forms.CharField(max_length=100,widget=forms.TextInput(attrs={'name':'expectednoticeperiod','class': "form-control",'placeholder': 'expectednoticeperiod'}))
    jobdescription=forms.CharField(max_length=100,widget=forms.TextInput(attrs={'name':'jobdescription','class': "form-control",'placeholder': 'jobdescription'}))
    domain=forms.CharField(max_length=100,widget=forms.TextInput(attrs={'name':'domain','class': "form-control",'placeholder': 'domain'}))
    joblocation=forms.CharField(max_length=100,widget=forms.TextInput(attrs={'name':'joblocation','class': "form-control",'placeholder': 'joblocation'}))
    contactname=forms.CharField(max_length=100,widget=forms.TextInput(attrs={'name':'contactname','class': "form-control",'placeholder': 'contactname'}))
    contactmailid=forms.CharField(max_length=100,widget=forms.TextInput(attrs={'name':'contactmailid','class': "form-control",'placeholder': 'contactmailid'}))
    contactmobilenumber=forms.CharField(max_length=100,widget=forms.TextInput(attrs={'name':'contactmobilenumber','class': "form-control",'placeholder': 'contactmobilenumber'}))
    payscalefromlacks=forms.ChoiceField(choices=[(x, x) for x in range(1900, 2020)],widget=forms.Select(attrs={'name':'payscalefromlacks','class': "form-control",'placeholder': 'payscalefromlacks'}))
    payscalefromthousand=forms.ChoiceField(choices=[(x, x) for x in range(1900, 2020)],widget=forms.Select(attrs={'name':'payscalefromthousand','class': "form-control",'placeholder': 'payscalefromthousand'}))
    payscaletolacks=forms.ChoiceField(choices=[(x, x) for x in range(1900, 2020)],widget=forms.Select(attrs={'name':'payscaletolacks','class': "form-control",'placeholder': 'payscaletolacks'}))
    payscaletothousand=forms.ChoiceField(choices=[(x, x) for x in range(1900, 2020)],widget=forms.Select(attrs={'name':'payscaletothousand','class': "form-control",'placeholder': 'payscaletothousand'}))
    contractjob=forms.CharField(max_length=100,widget=forms.TextInput(attrs={'name':'contractjob','class': "form-control",'placeholder': 'contractjob'}))
    contractfromyear=forms.ChoiceField(choices=[(x, x) for x in range(1900, 2020)],widget=forms.Select(attrs={'name':'contractfromyear','class': "form-control",'placeholder': 'contractfromyear'}))
    contractfrommonth=forms.ChoiceField(choices=[(x, x) for x in range(1900, 2020)],widget=forms.Select(attrs={'name':'contractfrommonth','class': "form-control",'placeholder': 'contractfrommonth'}))
    contracttoyear=forms.ChoiceField(choices=[(x, x) for x in range(1900, 2020)],widget=forms.Select(attrs={'name':'contracttoyear','class': "form-control",'placeholder': 'contracttoyear'}))
    contracttomonth=forms.ChoiceField(choices=[(x, x) for x in range(1900, 2020)],widget=forms.Select(attrs={'name':'contracttomonth','class': "form-control",'placeholder': 'contracttomonth'}))
