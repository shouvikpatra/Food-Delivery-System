from django.urls import path
from . import views

urlpatterns = [
    path('<int:rid>/', views.restaurant, name="restaurant"),
    path('<int:rid>/menu/', views.menu, name="menu"),
    path('<int:rid>/menu/add_dish/', views.add_dish, name="add_dish"),
    path('<int:rid>/menu/update_dish/<int:did>/',
         views.update_dish, name="update_dish"),
    path('<int:rid>/menu/delete_dish/<int:did>/',
         views.delete_dish, name="delete_dish"),


]
