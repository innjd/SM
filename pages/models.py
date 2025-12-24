from django.db import models

class User(models.Model):
    password = models.CharField(max_length=32)
    username = models.CharField(max_length=32)

class Post_Item(models.Model):
    upload_video = models.FileField(upload_to='uploads/', blank=True, null=True)
    image = models.ImageField(upload_to='images/', blank=True, null=True)

# class Profile(models.Model):
#     icon =
#     name = 
#     description =
#     sum_like =
#     subscribers =
#     subscribe_to =
