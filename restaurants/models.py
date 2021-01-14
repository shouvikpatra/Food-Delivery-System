from django.db import models

# Create your models here.


class Restaurant(models.Model):
    name = models.CharField(max_length=255, null=True)
    username = models.CharField(max_length=50, null=True)
    address = models.CharField(max_length=1500, null=True)
    contact = models.IntegerField(null=True)
    maxActiveOrders = models.IntegerField(null=True)

    def __str__(self):
        return str(self.id)


class Menu(models.Model):
    category = (('Chinese', 'Chinese'),
                ('North Indian', 'North Indian'),
                ('South Indian', 'South Indian'),
                ('Italian', 'Italian'),
                )
    res_id = models.ForeignKey(
        "Restaurant", on_delete=models.CASCADE)
    dish_name = models.CharField(max_length=255, null=True)
    price = models.FloatField(max_length=255, null=True)
    availability = models.BooleanField(default=True)
    cuisine = models.CharField(max_length=50, choices=category)
