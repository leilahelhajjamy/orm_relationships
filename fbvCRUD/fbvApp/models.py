from django.db import models

class Student(models.Model):
    firstName = models.CharField(max_length= 20 , default="")
    lastName = models.CharField(max_length= 20 , default="")
    testScore = models.FloatField()
# Create your models here.




class Programmer(models.Model):
    name = models.CharField(max_length=30)
    sal = models.IntegerField()


class Project(models.Model):
    name = models.CharField(max_length=30)
    programmers = models.ManyToManyField(Programmer)


class Customer(models.Model):
    name = models.CharField(max_length=30)


class PhoneNumber(models.Model):
    type = models.CharField(max_length=10)
    number = models.CharField(max_length=10)
    customer = models.ForeignKey(Customer , on_delete=models.CASCADE)