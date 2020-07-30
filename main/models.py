from django.db import models
from django.contrib.auth.models import User

class Blog(models.Model):
    objects=models.Manager()
    title = models.CharField(max_length=200)
    date = models.DateField('date published')
    body = models.TextField()
    #게시물의 좋아요 수
    like_num = models.PositiveIntegerField(default=0)
        #처음에는 좋아요 수가 0개이므로 default=0

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:20]

class Portfolio(models.Model):
    title = models.CharField(max_length=200)
    img = models.ImageField(upload_to="images/")
    body = models.CharField(max_length=200)

    def __str__(self):
        return self.title
# Create your models here.
#  