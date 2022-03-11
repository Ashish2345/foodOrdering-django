
from django.shortcuts import redirect, render, get_object_or_404
from .models import Catg_Foods, Food_Items
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.db.models import Q
from carts.models import Cart,CartItem
from carts.context_processor import _cart_id
from .models import Contact_Us, Food_pics
from accounts.forms import UserRegistrationForm

# Create your views here.
def main_page(request, slug=None):
    contex = UserRegistrationForm()
    categories = None
    food_Items = None
    food_Itemss = Food_Items.objects.all()[:3]
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
    
    context = {"reg":contex,
            'categories': categories,
        'food_Items': paged_product,
        'food_Itemss': food_Itemss}
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
    pics = Food_pics.objects.all().order_by("-id")
    context = {
        "pics":pics
    }
    return render(request, 'food_gallery.html',context)

def about_us(request):
    return render(request, 'about_us.html')

def food_details(request):
    return render(request, 'food_details.html')

def sucess(request):
    return render(request, 'sucess.html')

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

def checkout(request,total=0,quantity=0):
    current_user = request.user
    cart_items = CartItem.objects.filter(user=current_user)
    total=0 
    quantity=0
    for cart in cart_items:
        total += (cart.foodItems.food_price * cart.quantity)
        quantity += cart.quantity
    grand_total = total - 100
    context = {

        "total":total,
        "grand":grand_total
    }
    return render(request, 'checkout_address.html',context)
