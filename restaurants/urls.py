from django.urls import path
from . import views

urlpatterns = [
    path('<int:rid>', views.restaurant, name="restaurant"),
    path('<int:rid>/menu/', views.menu, name="menu"),
    path('<int:rid>/menu/add_dish/', views.add_dish, name="add_dish"),
    #path('<int:rid>/menu/add_item/', views.update_item, name="update_item"),
    #path('<int:rid>/menu/add_item/', views.delete_item, name="delete_item"),


]
