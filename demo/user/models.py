from django.db import models
from django.contrib.auth.models import User
# Create your models here.


# class xxUser(models.Model):
#     id = models.AutoField(auto_created=True, primary_key=True)
#     email = models.EmailField(unique=True)
#     name = models.CharField(max_length=100)

#     class Meta:
#         db_table = "xxUser"

class Music(models.Model):

    song = models.TextField()
    singer = models.TextField()
    last_modify_date = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "music"

class Share(models.Model):
    name = models.TextField()
    last_modify_date = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "share"