from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("",views.index,name = "ShopName"),
    path("about/" , views.about , name = "about"),
    path("contact/" , views.contacts , name = "contactUs"),
    path("tracker/" , views.track , name = "trackerStatus"),
    path("search/" , views.search , name = "search"),
    path("products/<int:myid>" , views.productview , name = "productview"),
    path("cheakout/" , views.cheak , name = "cheakout"),
    
]
