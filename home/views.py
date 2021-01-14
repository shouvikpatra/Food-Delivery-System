from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from restaurants.models import Restaurant

# Create your views here.


def home(request):
    return render(request, 'home/home.html')


def about(request):
    return render(request, 'home/about.html')


def cusRegister(response):
    return render(request, 'home/cusRegister.html')


def resRegister(response):
    if response.method == "POST" and response.POST['res_password'] == response.POST['res_confirm_password']:
        user = User.objects.create_user(
            username=response.POST['res_username'], password=response.POST['res_password'])
        user.save()

        ins = Restaurant(name=response.POST['res_name'], username=response.POST['res_username'], address=response.POST['res_address'],
                         contact=response.POST['res_contact_number'], maxActiveOrders=response.POST['res_max_active_order'])
        ins.save()

    return render(response, 'home/resRegister.html')
