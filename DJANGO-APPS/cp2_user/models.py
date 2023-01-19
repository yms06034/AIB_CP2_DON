from django.db import models

from django.contrib.auth.models import User as U

# Create your models here.

""" Test splite3 DB migrate """
class User(models.Model):
    name = models.CharField(max_length=20)
    nickname = models.CharField(max_length=100)
    update_at = models.DateTimeField(auto_now=True)
    create_at = models.DateTimeField(auto_now_add=True)

class UserDetail(models.Model):
    user = models.OneToOneField(U, on_delete=models.CASCADE)
    ture_user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
