from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class Technical(models.Model):
    title=models.CharField(max_length=100)
    content=models.TextField()
    like=models.IntegerField(default=True)
    dislike=models.IntegerField(default=True)
    # date_posted=models.DateTimeField(auto_now_add=True)
    date_posted=models.DateTimeField(default=timezone.now)
    author=models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('technical-detail',kwargs={'pk':self.pk})

class Comments(models.Model):
    comments=models.CharField(max_length=100)

    commentsauthor=models.ForeignKey(Technical,on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('technical-detail',kwargs={'pk':self.pk})
