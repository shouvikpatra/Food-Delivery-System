from django.db import models


# Create your models here.


class Order(models.Model):
    category = (('Confirmed', 'Confirmed'),
                ('Preparing', 'Preparing'),
                ('Out for Delivery', 'Out for Delivery'),
                ('Delivered', 'Delivered'),
                ('Cancelled', 'Cancelled'),
                )
    restaurant = models.ForeignKey(
        "restaurants.Restaurant", null=True, on_delete=models.SET_NULL)
    customer = models.ForeignKey(
        "customers.Customer", null=True, on_delete=models.SET_NULL)
    status = models.CharField(max_length=60, choices=category)
    order_activity = models.CharField(max_length=60, choices=(
        ('Active', 'Active'), ('Inactive', 'Inactive')))


class OrderList(models.Model):
    order_id = models.ForeignKey(
        "Order", null=True, on_delete=models.SET_NULL)
    dish_id = models.ForeignKey(
        "restaurants.Menu", null=True, on_delete=models.SET_NULL)
    dish_quantity = models.IntegerField(default=1)
