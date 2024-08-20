from django.db import models

# Create your models here.

class Client(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    telephone = models.BigIntegerField()
    create_time=models.DateTimeField(auto_now_add=True)
