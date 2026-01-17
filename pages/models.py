from django.db import models

class User(models.Model):
    password = models.CharField(max_length=32)
    username = models.CharField(max_length=32)

class Post_Item(models.Model):
    upload_video = models.FileField(upload_to='uploads/', blank=True, null=True)
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    text= models.CharField(max_length=1000)
    author = models.CharField(max_length=32)
class Message(models.Model):
    sender = models.CharField(max_length=32)
    receiver = models.CharField(max_length=32)
    text= models.CharField(max_length=1000)
class Chat(models.Model):
    user1=models.CharField(max_length=32)
    user2= models.CharField(max_length=32)
class Like(models.Model):
    item_id= models.IntegerField()
    user =models.CharField(max_length=32)

# class UserProfile(models.Model):
#     icon =models.ImageField(upload_to='icons/', blank=True, null=True)
#     name= models.CharField(max_length=32)
#     description=models.CharField(max_length=1000)
