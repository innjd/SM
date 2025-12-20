from django.db import models

class User(models.Model):
    password = models.CharField(max_length=32)
    username = models.CharField(max_length=32)
