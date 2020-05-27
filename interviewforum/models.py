from django.db import models
from django.utils import timezone
from django.urls import reverse
# Create your models here.


class Interview(models.Model):
    author=models.ForeignKey('auth.User',    on_delete=models.CASCADE)
    title=models.CharField(max_length=200)
    text=models.TextField()
    create_date=models.DateTimeField(default=timezone.now)
    published_date=models.DateTimeField(blank=True,null=True)

    def publish(self):
        self.published_date=timezone.now()

        self.save()

    def approve_interviewcomments(self):
        return self.interviewcomments.filter(approved_interviewcomment=True)

    def get_absolute_url(self):

        return reverse('interview_detail',kwargs={'pk':self.pk})

    def __str__(self):
        return self.title


class InterviewComments(models.Model):
    interview = models.ForeignKey('interviewforum.Interview',related_name='interviewcomments',on_delete=models.CASCADE)
    author=models.CharField(max_length=200)
    text=models.TextField()
    create_date=models.DateTimeField(default=timezone.now)
    approved_interviewcomment=models.BooleanField(default=False)

    def approve(self):
        self.approved_interviewcomment=True
        self.save()

    def get_absolute_url(self):
        return reverse('interview_list')

    def __str__(self):
        return self.text
