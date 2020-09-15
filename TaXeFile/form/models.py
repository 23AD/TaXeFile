from django.db import models


# Create your models here.
class form(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    email = models.EmailField()
    tel = models.BigIntegerField()
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    pincode = models.IntegerField()
    birthday = models.DateField()
    aadhar = models.BigIntegerField()
    file = models.FileField()
    pan = models.CharField(max_length=15)
    file1 = models.FileField()
    account = models.BigIntegerField()
    ifsccode = models.CharField(max_length=20)
