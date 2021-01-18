from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from orders.models import *
from .models import *
from .forms import *


# Create your views here.

@login_required(login_url='home')
def restaurant(response, rid):
    restaurant = Restaurant.objects.get(id=rid)
    orders = Order.objects.filter(restaurant_id=rid, order_activity=True)
    context = {'rid': rid, 'restaurant': restaurant,
               'orders': orders, }
    return render(response, 'restaurants/restaurant.html', context)


def resOrderPage(response, rid):
    restaurant = Restaurant.objects.get(id=rid)
    orders = Order.objects.filter(restaurant_id=rid)

    context = {'rid': rid, 'restaurant': restaurant,
               'orders': orders, }
    return render(response, 'restaurants/orderPage.html', context)


@login_required(login_url='home')
def menu(response, rid):
    dishes = Menu.objects.filter(res_id=rid)
    return render(response, 'restaurants/menu.html', {'dishes': dishes, 'rid': rid})


@login_required(login_url='home')
def resProfile(response, rid):
    profile = Restaurant.objects.get(id=rid)
    form = ProfileForm(instance=profile)
    print(profile.username)
    context = {'form': form, 'rid': rid, 'username': profile.username}
    return render(response, 'restaurants/myProfile.html', context)


@login_required(login_url='home')
def update_res_profile(response, rid):
    profile = Restaurant.objects.get(id=rid)
    if response.method == "POST":
        profile.name = response.POST['name']
        profile.address = response.POST['address']
        profile.contact = response.POST['contact']
        profile.maxActiveOrders = response.POST['maxActiveOrders']
        profile.save()
        return redirect('resProfile', rid=rid)
    return redirect('resProfile', rid=rid)


@login_required(login_url='home')
def delete_res_profile(response, rid):
    profile = Restaurant.objects.get(id=rid)
    print(profile.username)
    restaurant = User.objects.get(username=profile.username)
    print(restaurant.get_username())
    if response.method == "POST":
        restaurant.delete()
        return redirect('home')

    context = {'delObject': 'your Profile, ' +
               profile.name, 'prevPage': "resProfile", 'id': rid, 'rid': rid}
    return render(response, 'restaurants/delete.html', context)

# MENU FUNCTIONALITITES


@login_required(login_url='home')
def add_dish(response, rid):
    form = DishForm(initial={'res_id': rid})

    if response.method == "POST":
        ins = DishForm(response.POST, initial={'res_id': rid})
        if ins.is_valid():
            ins.save()
        return redirect('menu', rid=rid)

    context = {'form': form, 'rid': rid}
    return render(response, 'restaurants/dish.html', context)


@login_required(login_url='home')
def update_dish(response, rid, did):
    dish = Menu.objects.get(id=did)
    form = DishForm(instance=dish)
    if response.method == "POST":
        upd = DishForm(response.POST, instance=dish)
        if upd.is_valid():
            upd.save()
        return redirect('menu', rid=rid)
    context = {'form': form, 'rid': rid}
    return render(response, 'restaurants/dish.html', context)


@login_required(login_url='home')
def delete_dish(response, rid, did):
    form = Menu.objects.get(id=did)
    print(form.dish_name)
    if response.method == "POST":
        form.delete()
        return redirect('menu', rid=rid)
    context = {'delObject': form.dish_name,
               'prevPage': "menu", 'id': rid, 'rid': rid}
    return render(response, 'restaurants/delete.html', context)
