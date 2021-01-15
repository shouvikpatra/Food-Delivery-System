from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from .forms import DishForm

# Create your views here.


def restaurant(response, rid):
    dishes = Menu.objects.all()

    return render(response, 'restaurants/restaurant.html', {'dishes': dishes})


def menu(response, rid):
    dishes = Menu.objects.filter(res_id=rid)
    return render(response, 'restaurants/menu.html', {'dishes': dishes})


def add_dish(response, rid):
    form = DishForm()
    context = {'form': form}
    return render(response, 'restaurants/dish.html', context)


def update_item(response, rid):
    form = DishForm()
    context = {'form': form}
    return render(response, 'restaurants/dish.html', context)


def delete_item(response, rid):
    form = DishForm()
    context = {'form': form}
    return render(response, 'restaurants/dish.html', context)
