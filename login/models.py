from django.db import models
from django.contrib.auth.models import User
from main.models import Blog
# Create your models here.


class Account(models.Model):
    #장고 유저와 내가 만든 모델의 일대일 연결
    objects=models.Manager()
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nickname = models.CharField(max_length =10)
    email = models.CharField(max_length =50)

    like_blogs = models.ManyToManyField('main.Blog', blank=True, related_name = "like_user")
        #user가 처음 생길 때, 어떤 게시물과도 관계가 없으므로 blank=True
        #related_name으로 반대쪽 모델에 접근하기 위해

    def __str__(self):
        return self.nickname
