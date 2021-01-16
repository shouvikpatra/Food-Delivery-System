from django.urls import path
from . import views

urlpatterns = [
    path('<int:cid>/', views.customer, name="customer"),

    # Profile Urls
    path('<int:cid>/myProfile/', views.cusProfile, name="cusProfile"),
    path('<int:cid>/myProfile/update',
         views.update_cus_profile, name="update_cus_profile"),
    path('<int:cid>/myProfile/delete',
         views.delete_cus_profile, name="delete_cus_profile"),


]
