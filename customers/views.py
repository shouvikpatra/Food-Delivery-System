from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import *
from restaurants.models import *
from .forms import *
from .filters import *
# Create your views here.


@login_required(login_url='home')
def customer(response, cid):
    customer = Customer.objects.get(id=cid)

    context = {'cid': cid, 'customer': customer, }
    return render(response, 'customers/customer.html', context)


def showRestaurants(response, cid):
    customer = Customer.objects.get(id=cid)
    restaurants = Restaurant.objects.all()
    restaurantFilter = RestaurantFilter(response.GET, queryset=restaurants)
    restaurants = restaurantFilter.qs

    context = {'cid': cid, 'customer': customer,
               'restaurants': restaurants, 'restaurantFilter': restaurantFilter}
    return render(response, 'customers/showRestaurants.html', context)


def orderMenu(response, cid, rid):
    restaurant = Restaurant.objects.get(id=rid)
    menu = Menu.objects.filter(res_id=restaurant, availability=True)
    menuFilter = MenuFilter(response.GET, queryset=menu)
    menu = menuFilter.qs
    context = {'cid': cid, 'restaurant': restaurant,
               'menu': menu, 'menuFilter': menuFilter}
    return render(response, 'customers/orderMenu.html', context)

# Profile Options
@login_required(login_url='home')
def cusProfile(response, cid):
    profile = Customer.objects.get(id=cid)
    form = ProfileForm(instance=profile)
    context = {'cid': cid, 'form': form, 'username': profile.username}
    return render(response, 'customers/myProfile.html', context)


@login_required(login_url='home')
def update_cus_profile(response, cid):
    profile = Customer.objects.get(id=cid)
    if response.method == "POST":
        profile.name = response.POST['name']
        profile.address = response.POST['address']
        profile.contact = response.POST['contact']
        profile.save()
        return redirect('cusProfile', cid=cid)
    return redirect('cusProfile', cid=cid)


@login_required(login_url='home')
def delete_cus_profile(response, cid):
    profile = Customer.objects.get(id=cid)
    customer = User.objects.get(username=profile.username)
    if response.method == "POST":
        customer.delete()
        return redirect('home')

    context = {'delObject': 'your Profile, ' +
               profile.name, 'prevPage': "cusProfile", 'id': cid, 'cid': cid}
    return render(response, 'customers/delete.html', context)
