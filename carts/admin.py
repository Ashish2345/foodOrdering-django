import imp
from django.contrib import admin
from .models import Cart,CartItem

# Register your models here.
admin.site.register(Cart)

class CartAdmin(admin.ModelAdmin):
    list_display = ('user','foodItems','quantity')
admin.site.register(CartItem,CartAdmin)

