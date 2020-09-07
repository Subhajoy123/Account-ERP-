from django.db import models

# Create your models here.
class Director(models.Model):
    name: models.CharField(max_length=200)
    dob: models.CharField(max_length=200)
    number: models.IntegerField(default=0)
    share: models.CharField(max_length=200)
    education: models.TextField()
    din: models.IntegerField(default=0)
    gender: models.TextField()
    pan: models.IntegerField(default=0)
    occupation: models.TextField()
    