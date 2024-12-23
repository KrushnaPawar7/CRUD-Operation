from django.db import models

# Create your models here.
class Employee(models.Model):
    name=models.CharField(max_length=20)
    salary=models.IntegerField()
    position=models.CharField(max_length=20)
    blood_g=models.CharField(max_length=3)
    age=models.IntegerField()