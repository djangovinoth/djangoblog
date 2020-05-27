from django.contrib import admin
from .models import Interview,InterviewComments

# Register your models here.

admin.site.register(InterviewComments)
admin.site.register(Interview)
