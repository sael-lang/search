from datetime import date
import email
from django.db import models

# Create your models here.
class userdata(models.Model):
    username=models.CharField(max_length=15)
    fname=models.CharField(max_length=15)
    lname=models.CharField(max_length=15)
    password=models.CharField(max_length=25)
    email=models.CharField(max_length=25)
    phone=models.CharField(max_length=15)
    country=models.CharField(max_length=15)
    DOB=models.CharField(max_length=500)
    
class verification_data(models.Model):
    token=models.CharField(max_length=40)
    email=models.CharField(max_length=25)
    verified=models.BooleanField()

class companydata(models.Model):
    website=models.CharField(max_length=25)
    details=models.CharField(max_length=50)

class logindata(models.Model):
    username=models.CharField(max_length=15)
    fname=models.CharField(max_length=15)
    lname=models.CharField(max_length=15)

class scoredata(models.Model):
    username=models.CharField(max_length=15)
    scores=models.CharField(max_length=15)

class taskdata(models.Model):
    name=models.CharField(max_length=15)
    scores=models.CharField(max_length=15)
    date=models.CharField(max_length=15)

