from django.urls import path
from . import views

urlpatterns = [
    path('<int:cid>/', views.customer, name="customer"),

    # Restaurants Tab
    path('<int:cid>/showRestaurants/',
         views.showRestaurants, name="showRestaurants"),
    # Restaurant Menu Page
    path('<int:cid>/showRestaurants/res<int:rid>/',
         views.orderMenu, name="orderMenu"),
    path('<int:cid>/showRestaurants/res<int:rid>/dish_add<int:did>/',
         views.add_to_cart, name="add_to_cart"),
    path('<int:cid>/showRestaurants/res<int:rid>/dish_inc<int:did>/',
         views.inc_quantity_m, name="inc_quantity_m"),
    path('<int:cid>/showRestaurants/res<int:rid>//dish_dcr<int:did>/',
         views.dcr_quantity_m, name="dcr_quantity_m"),


    # My Cart Tab
    path('<int:cid>/myCart/', views.myCart, name="myCart"),
    path('<int:cid>/myCart/dish<int:did>/inc',
         views.inc_quantity, name="inc_quantity"),
    path('<int:cid>/myCart/dish<int:did>/dcr',
         views.dcr_quantity, name="dcr_quantity"),
    path('<int:cid>/myCart/placeOrder/', views.placeOrder, name="placeOrder"),

    # Order
    path('<int:cid>/myOrders/', views.cusOrderPage, name="cusOrderPage"),


    # Profile Urls
    path('<int:cid>/myProfile/', views.cusProfile, name="cusProfile"),
    path('<int:cid>/myProfile/update',
         views.update_cus_profile, name="update_cus_profile"),
    path('<int:cid>/myProfile/delete',
         views.delete_cus_profile, name="delete_cus_profile"),


]
