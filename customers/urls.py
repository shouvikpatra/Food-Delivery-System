from django.urls import path
from . import views

urlpatterns = [
    path('<int:cid>/', views.customer, name="customer"),

]
