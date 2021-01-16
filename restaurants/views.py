from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from .models import *
from .forms import DishForm, ProfileForm

# Create your views here.


def restaurant(response, rid):
    dishes = Menu.objects.all()
    return render(response, 'restaurants/restaurant.html', {'dishes': dishes})


def menu(response, rid):
    dishes = Menu.objects.filter(res_id=rid)
    return render(response, 'restaurants/menu.html', {'dishes': dishes, 'rid': rid})


def resProfile(response, rid):
    profile = Restaurant.objects.get(id=rid)
    form = ProfileForm(instance=profile)
    context = {'form': form, 'rid': rid}
    return render(response, 'restaurants/myProfile.html', context)


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


def delete_res_profile(response, rid):
    profile = Restaurant.objects.get(id=rid)
    print(profile.username)
    restaurant = User.objects.get(username=profile.username)
    print(restaurant.get_username())
    if response.method=="POST":
        restaurant.delete()
        return redirect('home')

    context = {'delObject': 'your Profile, ' +
               profile.name, 'prevPage': "resProfile", 'id': rid}
    return render(response, 'restaurants/delete.html', context)

# MENU FUNCTIONALITITES


def add_dish(response, rid):
    form = DishForm(initial={'res_id': rid})

    if response.method == "POST":
        ins = DishForm(response.POST, initial={'res_id': rid})
        if ins.is_valid():
            ins.save()
        return redirect('menu', rid=rid)

    context = {'form': form}
    return render(response, 'restaurants/dish.html', context)


def update_dish(response, rid, did):
    dish = Menu.objects.get(id=did)
    form = DishForm(instance=dish)
    if response.method == "POST":
        upd = DishForm(response.POST, instance=dish)
        if upd.is_valid():
            upd.save()
        return redirect('menu', rid=rid)
    context = {'form': form}
    return render(response, 'restaurants/dish.html', context)


def delete_dish(response, rid, did):
    form = Menu.objects.get(id=did)
    print(form.dish_name)
    if response.method == "POST":
        form.delete()
        return redirect('menu', rid=rid)
    context = {'delObject': form.dish_name, 'prevPage': "menu", 'id': rid}
    return render(response, 'restaurants/delete.html', context)
