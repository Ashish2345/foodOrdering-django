from django.urls import path
from . import views

urlpatterns = [
    path("", views.cart, name="cart"),
    path("add-cart/<int:food_id>", views.add_cart, name="add_cart"),
    path("remove-cart/<int:food_id>", views.minus_cart, name="minus_cart"),
    path("delete-cart/<int:food_id>", views.delete_cart, name="delete_cart")



]
