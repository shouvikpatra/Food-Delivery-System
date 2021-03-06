from django.urls import path
from . import views

urlpatterns = [
    path('<int:rid>/', views.restaurant, name="restaurant"),
    # Order URLs
    path('<int:rid>/myOrders/', views.resOrderPage, name="resOrderPage"),
    path('<int:rid>/myOrders/update_order/<int:oid>/',
         views.updateOrder, name="updateOrder"),


    # Menu URLs
    path('<int:rid>/menu/', views.menu, name="menu"),
    path('<int:rid>/menu/add_dish/', views.add_dish, name="add_dish"),
    path('<int:rid>/menu/update_dish/<int:did>/',
         views.update_dish, name="update_dish"),
    path('<int:rid>/menu/delete_dish/<int:did>/',
         views.delete_dish, name="delete_dish"),

    # Profile Urls
    path('<int:rid>/myProfile/', views.resProfile, name="resProfile"),
    path('<int:rid>/myProfile/update',
         views.update_res_profile, name="update_res_profile"),
    path('<int:rid>/myProfile/delete',
         views.delete_res_profile, name="delete_res_profile"),




]
