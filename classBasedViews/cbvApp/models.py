from django.db import models

class Student(models.Model):
    firstName = models.CharField(max_length= 20 , default="")
    lastName = models.CharField(max_length= 20 , default="")
    testScore = models.FloatField()
# Create your models here.
