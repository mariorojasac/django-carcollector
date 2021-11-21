from django.db import models

# Create your models here.

class Car(models.Model):
    model = models.CharField(max_length=100)
    make = models.CharField(max_length=100)
    description = models.TextField()
    milage = models.IntegerField()
    price = models.IntegerField()

