from django.contrib import admin
from .models import *


class RestaurantAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'username')
    exclude = ('id',)


class MenuAdmin(admin.ModelAdmin):
    list_display = ('id', 'res_id', 'dish_name', 'price', 'availability')
    exclude = ('id',)


# Register your models here.
admin.site.register(Restaurant, RestaurantAdmin)
admin.site.register(Menu, MenuAdmin)
