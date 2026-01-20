from django.db import models

# Create your models here.

class StudentModel(models.Model):
    name = models.CharField(max_length=30)
    sub = models.CharField(max_length=30)
    age = models.IntegerField()
    email = models.EmailField(unique= True)

    