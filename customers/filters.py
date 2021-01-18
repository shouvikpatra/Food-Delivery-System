import django_filters
from django.db import models

from restaurants.models import Restaurant, Menu
from orders.models import Order


class RestaurantFilter(django_filters.FilterSet):
    class Meta:
        model = Restaurant
        fields = '__all__'
        exclude = ['username', 'contact', 'maxActiveOrders']
        filter_overrides = {
            models.CharField: {
                'filter_class': django_filters.CharFilter,
                'extra': lambda f: {
                    'lookup_expr': 'icontains',
                },
            }, }


class MenuFilter(django_filters.FilterSet):
    class Meta:
        model = Menu
        fields = '__all__'
        filter_overrides = {
            models.CharField: {
                'filter_class': django_filters.CharFilter,
                'extra': lambda f: {
                    'lookup_expr': 'icontains',
                },
            }, }


class OrderFilter(django_filters.FilterSet):
    class Meta:
        model = Order
        fields = '__all__'
        exclude = ['dish', 'quantity']
        filter_overrides = {
            models.CharField: {
                'filter_class': django_filters.CharFilter,
                'extra': lambda f: {
                    'lookup_expr': 'icontains',
                },
            }, }
