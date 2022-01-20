from django.urls import path
from . import views


urlpatterns = [
   path('',views.main_page,name='mainpage'),
   path('menu/',views.our_menu,name='our_menu'),
   path('menu/<slug:slug>',views.our_menu,name='our_catg'),
   path('menu/<slug:slug>/<slug:foodslug>/',views.food_detail,name='food_detail'),
  
   path('food_gallery/',views.food_gallery,name='food_gallery'),
   path('about_us/',views.about_us,name='about_us'),
   path('food_details/',views.food_details,name='food_details'),
   path('contact_us/',views.contact_us,name='contact_us'),
   path('login/',views.login,name='login'),



]
