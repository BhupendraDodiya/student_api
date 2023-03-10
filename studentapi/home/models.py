from django.db import models

# Create your models here.
class Student(models.Model):
    Name = models.CharField(max_length=100)
    Roll_No = models.IntegerField()
    Contact = models.IntegerField()