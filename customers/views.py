from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from .models import *
from .forms import *
# Create your views here.


def customer(response, cid):
    customer = Customer.objects.get(id=cid)
    print(type(customer.name))

    context = {'cid': cid, 'customer': customer}
    return render(response, 'customers/customer.html', context)


def cusProfile(response, cid):
    profile = Customer.objects.get(id=cid)
    form = ProfileForm(instance=profile)
    context = {'cid': cid, 'form': form, 'username': profile.username}
    return render(response, 'customers/myProfile.html', context)


def update_cus_profile(response, cid):
    profile = Customer.objects.get(id=cid)
    if response.method == "POST":
        profile.name = response.POST['name']
        profile.address = response.POST['address']
        profile.contact = response.POST['contact']
        profile.save()
        return redirect('cusProfile', cid=cid)
    return redirect('cusProfile', cid=cid)


def delete_cus_profile(response, cid):
    profile = Customer.objects.get(id=cid)
    customer = User.objects.get(username=profile.username)
    if response.method == "POST":
        customer.delete()
        return redirect('home')

    context = {'delObject': 'your Profile, ' +
               profile.name, 'prevPage': "cusProfile", 'id': cid, 'cid': cid}
    return render(response, 'customers/delete.html', context)
