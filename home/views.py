from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.models import User
from restaurants.models import Restaurant
from customers.models import Customer

# Create your views here.


def home(request):
    return render(request, 'home/home.html')


def about(request):
    return render(request, 'home/about.html')


def cusRegister(response):
    if response.method == "POST" and response.POST['cus_password'] == response.POST['cus_confirm_password']:

        user = User.objects.create_user(
            username=response.POST['cus_username'], password=response.POST['cus_password'])
        user.save()

        ins = Customer(name=response.POST['cus_name'], username=response.POST['cus_username'], address=response.POST['cus_address'],
                       contact=response.POST['cus_contact_number'])
        ins.save()

        return redirect('/')

    return render(response, 'home/cusRegister.html')


def resRegister(response):
    if response.method == "POST" and response.POST['res_password'] == response.POST['res_confirm_password']:

        user = User.objects.create_user(
            username=response.POST['res_username'], password=response.POST['res_password'])
        user.save()

        ins = Restaurant(name=response.POST['res_name'], username=user, address=response.POST['res_address'],
                         contact=response.POST['res_contact_number'], maxActiveOrders=response.POST['res_max_active_order'])
        ins.save()

        return redirect('/')

    return render(response, 'home/resRegister.html')
