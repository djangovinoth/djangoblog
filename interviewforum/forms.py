from django import forms
from .models import Interview,InterviewComments

class InterviewForm(forms.ModelForm):

    class Meta():
        model=Interview
        fields=('title','text')

        # widgets={
        # 'title':forms.TextInput(attrs={'class':'textinputclass'}),
        # 'text':forms.Textarea(attrs={'class':'editable medium-editor-textarea postcontent'})
        #
        # }

class InterviewCommentForm(forms.ModelForm):
    class Meta():
        model=InterviewComments
        fields=('author','text')

        # widgets={
        # 'author':forms.TextInput(attrs={'class':'textinputclass'}),
        # 'text':forms.Textarea(attrs={'class':'editable medium-editor-textarea '})
        #
        # }
