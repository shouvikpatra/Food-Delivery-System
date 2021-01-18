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
    # My Cart Tab
    path('<int:cid>/myCart/', views.myCart, name="myCart"),
    path('<int:cid>/myCart/dish<int:did>/inc',
         views.inc_quantity, name="inc_quantity"),
    path('<int:cid>/myCart/dish<int:did>/dcr',
         views.dcr_quantity, name="dcr_quantity"),


    # Profile Urls
    path('<int:cid>/myProfile/', views.cusProfile, name="cusProfile"),
    path('<int:cid>/myProfile/update',
         views.update_cus_profile, name="update_cus_profile"),
    path('<int:cid>/myProfile/delete',
         views.delete_cus_profile, name="delete_cus_profile"),


]
