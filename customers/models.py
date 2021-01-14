from django.db import models

# Create your models here.


class Customer(models.Model):
    name = models.CharField(max_length=255, null=True)
    username = models.CharField(max_length=50, null=True)
    address = models.CharField(max_length=1500, null=True)
    contact = models.IntegerField(null=True)
    orders = models.IntegerField(default=0)
