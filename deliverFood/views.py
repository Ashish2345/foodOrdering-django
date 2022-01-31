
from django.http import HttpResponse
from django.shortcuts import redirect, render, get_object_or_404
from .models import Catg_Foods, Food_Items
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.db.models import Q
from carts.models import Cart,CartItem
from carts.context_processor import _cart_id
from django.core.exceptions import ObjectDoesNotExist
from .models import Contact_Us
from accounts.forms import UserRegistrationForm



# Create your views here.
def main_page(request):
    contex = UserRegistrationForm()
    context = {"reg":contex}
    return render(request, 'index.html',context)


def our_menu(request, slug=None):
    categories = None
    food_Items = None
    if(slug != None):
        categories = get_object_or_404(Catg_Foods, slug=slug)
        food_Items = Food_Items.objects.filter(
            category=categories, is_available=True)
        paginator = Paginator(food_Items, 6)
        page = request.GET.get('page')
        paged_product = paginator.get_page(page)
    else:
        food_Items = Food_Items.objects.all().filter(is_available=True).order_by("-id")
        paginator = Paginator(food_Items, 6)
        page = request.GET.get('page')
        paged_product = paginator.get_page(page)

    context = {
        'categories': categories,
        'food_Items': paged_product,

    }

    return render(request, 'ourmenu.html', context)


def food_detail(request, slug, foodslug,total=0, quantity=0, cart_items=None):
    try:
        food_detail = Food_Items.objects.get(
            category__slug=slug, slug=foodslug)
        
     
    except Exception as e:
        raise e
    context = {
        'food_detail': food_detail,
        
        }
    return render(request, 'food_details.html', context)

def search(request):
    if 'keyword' in request.GET:
        keyword = request.GET["keyword"]

        if keyword:
            food_Items = Food_Items.objects.order_by(
                "-id").filter(Q(food_desc__icontains=keyword) | Q(food_name__icontains=keyword))

    context = {
        'food_Items': food_Items
    }
    return render(request, 'ourmenu.html', context)


def food_gallery(request):
    return render(request, 'food_gallery.html')


def about_us(request):
    return render(request, 'about_us.html')


def food_details(request):
    return render(request, 'food_details.html')


def contact_us(request):
    
    
    if request.method == "POST":

        name = request.POST.get("name")
        print(name)
        email = request.POST.get("email")
        subject = request.POST.get("subject")
        comments = request.POST.get("comments")
        form = Contact_Us(user_name = name,user_email=email,subject=subject,message=comments)
        form.save()
        return redirect("mainpage")

       

    return render(request, 'contact_us.html')


def login(request):
    return render(request, 'login.html')
