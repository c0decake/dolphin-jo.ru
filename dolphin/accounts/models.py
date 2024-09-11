from django.contrib.auth.models import AbstractUser
from django.db import models


class Users(AbstractUser):
    father_name = models.CharField(max_length=100, null=True)
    phone = models.CharField(max_length=15, null=True)
    telegram_id = models.CharField(max_length=20)
    post = models.ForeignKey(to='Post', on_delete=models.SET_NULL, null=True)


class Post(models.Model):
    name = models.CharField(max_length=50, null=True)
