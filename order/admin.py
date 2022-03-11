from django.contrib import admin
from .models import Order
from django.utils.html import format_html

# Register your models here.

class OrderAdmin(admin.ModelAdmin):
    list_display = ["order_number","first_name","phone","email","address","order_total","created_at","click_me"]
    list_filter = ["status"]
    search_fields = ["order_number","first_name","phone","email"]
    
    def click_me(self,obj):
        return format_html("<button onclick='window.print()'>Print</button>")



admin.site.register(Order,OrderAdmin)