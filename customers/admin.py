from django.contrib import admin
from .models import *


class CustomerAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'username')
    exclude = ('id',)


'''
class CartAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'username')
    exclude = ('id',)
'''


# Register your models here.
admin.site.register(Customer, CustomerAdmin)
#admin.site.register(Cart, CartAdmin)
