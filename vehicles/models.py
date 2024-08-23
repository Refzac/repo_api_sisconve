from django.db import models

# Create your models here.
class Vehicle(models.Model):
    clientid =models.BigIntegerField()
    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    year = models.IntegerField()
    matricula = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    color = models.CharField(max_length=50)
    create_time=models.DateTimeField(auto_now_add=True)
    update_time=models.DateTimeField(auto_now=True)
