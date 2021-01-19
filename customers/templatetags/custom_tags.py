from django import template
from ..models import *


register = template.Library()


@register.filter
def multiply(value1, value2):
    return value1*value2


@register.simple_tag
def totalprice(orders):
    total = 0
    for d in orders:
        total += d.dish.price*d.quantity

    return total


@register.simple_tag
def isAlreadyInCart(dish, cid):

    item = Cart.objects.get(dish_id=dish, customer_id=cid)
    if item:
        return True
    else:
        return False
