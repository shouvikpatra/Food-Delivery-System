from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from .models import *
# Create your views here.


def customer(response, cid):
    return HttpResponse("Customer")
