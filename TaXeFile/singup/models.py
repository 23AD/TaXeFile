from django.db import models


# Create your models here.
class singup(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    username = models.CharField(max_length=10)
    email = models.EmailField()
    password = models.CharField(max_length=7)
