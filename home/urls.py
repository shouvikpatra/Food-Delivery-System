from django.urls import path
from . import views

urlpatterns = [
    # Home Page URLs
    path('', views.home, name="home"),
    path('about/', views.about, name="about"),
    # Registrations
    path('customer-registration/', views.cusRegister,
         name="customer-registration"),
    path('restaurant-registration/', views.resRegister,
         name="restaurant-registration"),


]
