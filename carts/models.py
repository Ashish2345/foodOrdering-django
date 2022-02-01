import imp
from statistics import mode
from tabnanny import verbose
from xml.parsers.expat import model
from django.db import models
from deliverFood.models import Food_Items
from django.contrib.auth.models import User

# Create your models here.


class Cart(models.Model):
    cart_id = models.CharField(max_length=200, blank=True)
    date_added = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name = "cart"
        verbose_name_plural = "carts"

    def __str__(self):
        return self.cart_id


class CartItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    foodItems = models.ForeignKey(Food_Items, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE,null=True)
    quantity = models.IntegerField()

    def sub_total(self):
        return self.foodItems.food_price * self.quantity

    class Meta:
        verbose_name = "cartItem"
        verbose_name_plural = "cartItems"
