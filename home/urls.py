from django.urls import path, include
from . import views

urlpatterns = [
    # Home Page URLs
    path('', views.home, name="home"),
    path(r'^logout/$', views.logoutUser, name="logout"),
    path('about/', views.about, name="about"),
    # Registrations
    path('customer-registration/', views.cusRegister,
         name="customer-registration"),
    path('restaurant-registration/', views.resRegister,
         name="restaurant-registration"),

    # login Pages
    path('res-login/', views.reslogin, name="reslogin"),
    path('cus-login/', views.cuslogin, name="cuslogin"),
    path('restaurant/', include('restaurants.urls')),
    path('customer/', include('customers.urls')),


]
