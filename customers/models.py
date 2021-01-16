from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Customer(models.Model):
    name = models.CharField(max_length=255, null=True)
    username = models.ForeignKey(
        User, on_delete=models.CASCADE)
    address = models.CharField(max_length=1500, null=True)
    contact = models.IntegerField(null=True)
    orders = models.IntegerField(default=0)
