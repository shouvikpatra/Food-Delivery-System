from django.contrib import admin
from .models import *


class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'restaurant', 'customer', 'status', 'order_activity')


class OrderListAdmin(admin.ModelAdmin):
    list_display = ('id', 'order', 'dish', 'quantity',)


# Register your models here.
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderList, OrderListAdmin)
