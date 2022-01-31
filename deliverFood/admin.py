from django.contrib import admin
from .models import Catg_Foods,Food_Items,Contact_Us

# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('catg_name',)}
    list_display = ('catg_name','slug')

admin.site.register(Catg_Foods,CategoryAdmin)

class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('food_name',)}
    list_display = ('food_name','food_price','category','slug','modified_date','is_available')
    list_filter = ('category','is_available',)



admin.site.register(Food_Items,ProductAdmin)

class ContactAdmin(admin.ModelAdmin):
    list_display = ('user_name','user_email','subject','date')
    

admin.site.register(Contact_Us,ContactAdmin)
