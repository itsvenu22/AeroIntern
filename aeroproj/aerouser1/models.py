from django.db import models

# Create your models here.
class userdata(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    phonenumber = models.IntegerField(null=True)
    joindate = models.DateField(null=True)