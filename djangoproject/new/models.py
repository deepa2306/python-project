from django.db import models

# Create your models here.
class student(models.Model):
    name=models.CharField(max_length=15)
    email=models.EmailField(max_length=25)
    phone=models.CharField(max_length=15)
