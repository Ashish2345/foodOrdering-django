from urllib import request
from django.shortcuts import redirect, render
from carts.models import CartItem
from order.forms import OrderForm
from order.models import Order
from deliverFood.models import Food_Items
import datetime
# Create your views here.
def place_order(request,total=0,quantity=0):
    current_user = request.user

    cart_items = CartItem.objects.filter(user=current_user)
    cart_count = cart_items.count()
    total=0 
    quantity=0
    

    for cart in cart_items:
        total += (cart.foodItems.food_price * cart.quantity)
        quantity += cart.quantity
    grand_total = total - 100
    if cart_count <= 0:
        return redirect("our_menu")
    
    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            data = Order()
            data.user = current_user
            data.first_name = form.cleaned_data["first_name"]
            data.last_name = form.cleaned_data["last_name"]
            data.phone = form.cleaned_data["phone"]
            data.email = form.cleaned_data["email"]
            data.address = form.cleaned_data["address"]
            data.order_total = form.cleaned_data["order_note"]
            data.order_total = grand_total
            data.ip = request.META.get("REMOTE_ADDR")
            data.save()
            # Generate Order numebers
            yearr = int(datetime.date.today().strftime("%Y"))
            datee = int(datetime.date.today().strftime("%d"))
            monthss = int(datetime.date.today().strftime("%m"))
            dee = datetime.date(yearr,datee,monthss)
            current_Date = dee.strftime("%Y%d%m")
            order_number = current_Date + str(data.id)
            data.order_number = order_number
            data.save()
            CartItem.objects.filter(user= request.user).delete()
            return redirect("sucess")
        else:
            return redirect("checkout")