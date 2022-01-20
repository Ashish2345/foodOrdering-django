from django.shortcuts import render,get_object_or_404
from .models import Catg_Foods,Food_Items

# Create your views here.
def main_page(request):    
    return render(request,'index.html')
   

def our_menu(request,slug=None): 
    categories=None
    food_Items=None
    if(slug != None):
        categories = get_object_or_404(Catg_Foods,slug=slug)
        food_Items = Food_Items.objects.filter(category=categories,is_available=True)
    else:
        food_Items = Food_Items.objects.all().filter(is_available=True)

    context = {
        'categories':categories,
        'food_Items':food_Items
    }

    return render(request,'ourmenu.html',context)

def food_detail(request,slug,foodslug):    
    try:
        food_detail = Food_Items.objects.get(category__slug=slug,slug=foodslug)
    except Exception as e:
        raise e
    context = {'food_detail':food_detail}
    return render(request,'food_details.html',context)





def food_gallery(request):     
    return render(request,'food_gallery.html')


def about_us(request):     
    return render(request,'about_us.html')

def food_details(request):     
    return render(request,'food_details.html')


def contact_us(request):     
    return render(request,'contact_us.html')


def login(request):     
    return render(request,'login.html')
