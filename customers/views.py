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
    cart = Cart.objects.filter(customer_id=cid)
    dishes = []
    for c in cart:
        dishes = Menu.objects.get(id=c.dish.id)
    restaurant = Restaurant.objects.get(id=rid)
    menu = Menu.objects.filter(res_id=restaurant, availability=True)
    menuFilter = MenuFilter(response.GET, queryset=menu)
    menu = menuFilter.qs
    context = {'cid': cid, 'restaurant': restaurant,
               'menu': menu, 'menuFilter': menuFilter, 'rid': rid, 'cart': dishes}
    return render(response, 'customers/orderMenu.html', context)


def myCart(response, cid):
    customer = Customer.objects.get(id=cid)
    cartItems = Cart.objects.filter(customer=customer)
    restaurant = None
    total = None
    if cartItems.first():
        restaurant = cartItems.first().restaurant
        total = 0
        for c in cartItems:
            total += (c.dish.price*c.quantity)

    context = {'cid': cid, 'customer': customer,
               'restaurant': restaurant, 'cartItems': cartItems, 'totalprice': total}
    return render(response, 'customers/myCart.html', context)


def add_to_cart(response, cid, rid, did):
    customer = Customer.objects.get(id=cid)
    restaurant = Restaurant.objects.get(id=rid)
    dish = Menu.objects.get(id=did)
    cartItem = Cart(customer=customer, restaurant=restaurant, dish=dish)
    cartItem.save()
    return redirect('orderMenu', cid=cid, rid=rid)


def inc_quantity(response, cid, did):
    cartItem = Cart.objects.get(id=did)
    if cartItem.dish.availability == True:
        cartItem.quantity += 1
        cartItem.save()
    else:
        cartItem.delete()
    return redirect('myCart', cid=cid)


def dcr_quantity(response, cid, did):
    cartItem = Cart.objects.get(id=did)
    cartItem.quantity -= 1
    if cartItem.dish.availability == False or cartItem.quantity == 0:
        cartItem.delete()
    else:
        cartItem.save()
    return redirect('myCart', cid=cid)

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
