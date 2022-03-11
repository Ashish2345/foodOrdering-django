
from django.http import request
from django.shortcuts import render, redirect, get_object_or_404
from deliverFood.models import Food_Items
from .models import Cart, CartItem
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required

# Create your views here.
def _cart_id(request):
    cart = request.session.session_key
   
    if not cart:
        cart = request.session.create()
    return cart


def add_cart(request, food_id):
    current_user = request.user 
    foodItems = Food_Items.objects.get(
        id=food_id)  # get food id from food models
    if current_user.is_authenticated:
      
        try:
            cart_item = CartItem.objects.get(foodItems=foodItems, user=current_user)
            cart_item.quantity += 1
            cart_item.save()
        except CartItem.DoesNotExist:
            cart_item = CartItem.objects.create(
                foodItems=foodItems,
                user=current_user,
                quantity=1
            )
            cart_item.save()

        return redirect("cart")
        
    else:
        try:
            # get the cart using cat id which is the session
            cart = Cart.objects.get(cart_id=_cart_id(request))
        except Cart.DoesNotExist:
            cart = Cart.objects.create(
                cart_id=_cart_id(request)
            )
        cart.save()
        try:
            cart_item = CartItem.objects.get(foodItems=foodItems, cart=cart)
            cart_item.quantity += 1
            cart_item.save()
        except CartItem.DoesNotExist:
            cart_item = CartItem.objects.create(
                foodItems=foodItems,
                cart=cart,
                quantity=1
            )
            cart_item.save()

        return redirect("cart")


def minus_cart(request, food_id):
   
    foodItems = get_object_or_404(Food_Items, id=food_id)
    try:
        if request.user.is_authenticated:
            cart_items = CartItem.objects.get(foodItems=foodItems, user=request.user)
        else:
            cart = Cart.objects.get(cart_id=_cart_id(request))
            cart_items = CartItem.objects.get(foodItems=foodItems, cart=cart)
        if cart_items.quantity >= 1:
            cart_items.quantity -= 1
            cart_items.save()
        else:
            cart_items.delete()
    except:
        pass

    return redirect("cart")


def delete_cart(request, food_id):
  
    foodItems = get_object_or_404(Food_Items, id=food_id)
    if request.user.is_authenticated:
       cart_items = CartItem.objects.get(foodItems=foodItems, user=request.user)
    else:      
        cart = Cart.objects.get(cart_id=_cart_id(request)) 
        cart_items = CartItem.objects.get(foodItems=foodItems, cart=cart)
    cart_items.delete()
    return redirect("cart")


def cart(request, total=0, quantity=0, cart_items=None):
    try:
        if request.user.is_authenticated:
            cart_items = CartItem.objects.filter(user=request.user)
        else:
            cart = Cart.objects.get(cart_id=_cart_id(request))
            cart_items = CartItem.objects.filter(cart=cart)
        for cart in cart_items:
            total += (cart.foodItems.food_price * cart.quantity)
            quantity += cart.quantity
    except ObjectDoesNotExist:
        pass
    context = {
        'total': total,
        'quantity': quantity,
        'cart_items': cart_items

    }

    return render(request, "cart.html", context)

def print(request, total=0, quantity=0, cart_items=None):
    try:
        if request.user.is_authenticated:
            cart_items = CartItem.objects.filter(user=request.user)
        else:
            cart = Cart.objects.get(cart_id=_cart_id(request))
            cart_items = CartItem.objects.filter(cart=cart)
        for cart in cart_items:
            total += (cart.foodItems.food_price * cart.quantity)
            quantity += cart.quantity
    except ObjectDoesNotExist:
        pass
    context = {
        'total': total,
        'quantity': quantity,
        'cart_items': cart_items

    }
    return render(request, "print.html",context)