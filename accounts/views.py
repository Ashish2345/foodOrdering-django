
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.contrib import messages

from carts.models import Cart,CartItem
from .forms import UserRegistrationForm
from django.contrib.auth.decorators import login_required
import requests

#Sending tokens for verifying user registration
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode,urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import EmailMessage
from carts.models import Cart
from carts.views import _cart_id
# Create your views here.

def logins(request):
    
    if request.method == "POST":
       username = request.POST["username"]
       passwords = request.POST["password"]
       try:
           email = User.objects.get(username=username)
          
       except:
            messages.warning(request,"Email doesnot exists")
        
       log = authenticate(request,username=username,password=passwords)
       if log is not None:
           try:
               cart = Cart.objects.get(cart_id=_cart_id(request))
               is_Cart_item_exists = CartItem.objects.filter(cart=cart).exists()
               if is_Cart_item_exists:
                   cart_items = CartItem.objects.filter(cart=cart)                  
                   for item in cart_items:
                       item.user = log
                       item.save()
           except:
                print("Error")

           login(request, log)
           messages.success(request,"You are now logged in")
           url = request.META.get('HTTP_REFERER')
           try:
                query = requests.utils.urlparse(url).query
               
                params = dict(x.split("=") for x in query.split('&'))
                if 'next' in params:
                    nextPage =params['next']
                    return redirect(nextPage)         
           except:
                return redirect("mainpage")
       else:
            messages.warning(request,"Login Unsuccessful")
            return redirect("login")

    return render(request,"login.html",{"page":"login"})

def register(request):
  page = 'register'
  contex = UserRegistrationForm()
  if request.method == "POST":
       forms = UserRegistrationForm(request.POST)  
       if forms.is_valid():
           username = forms.cleaned_data['username']
           email = forms.cleaned_data['email']
           password = forms.cleaned_data['password1']
          
           user = User.objects.create_user(username=username,email=email,password=password,is_active=False)
           user.save()
           
           current_site = get_current_site(request)
           print(current_site)
           mail_subject = "Please activate your account"
           message = render_to_string("message.html",{
               'user':forms,
               'domain':current_site,
               'uuid':urlsafe_base64_encode(force_bytes(user.id)),
               'token':default_token_generator.make_token(user),
           })
           to_email = email
           send_email = EmailMessage(mail_subject,message,to=[to_email])
           send_email.send()        
           return redirect("/account/login/?command=verification&email="+email)
       else:
           messages.warning(request,"Registration Unsuccessful")
  context = {"reg":contex,"page":"register"}
  return render(request,"login.html",context)


       
def activate(request,uidb64,token):
    try:
        uuid = urlsafe_base64_decode(uidb64).decode()
        user = User._default_manager.get(pk=uuid)
    except(TypeError,ValueError,OverflowError):
        user = None
    if user is not None and default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()

        return redirect("login")
    else:
        messages.warning(request,"Invalid user token")
        
def logoutUser(request):
    logout(request)
    return redirect ("mainpage")

@login_required(login_url='login')
def dashboard(request):
    return render(request,"dashboard.html")

def forgetpasswords(request):
    if(request.method == "POST"):
        email = request.POST["email"]
        print(email)
        if(User.objects.filter(email=email).exists()):
            users = User.objects.get(email__iexact=email)
            #Reset Password link in Email
            current_site = get_current_site(request)         
            mail_subject = "Reset Your Password!!"
            message = render_to_string("reset_password.html",{
               'user':users,
               'domain':current_site,
               'uuid':urlsafe_base64_encode(force_bytes(users.id)),
               'token':default_token_generator.make_token(users),
           })
            to_email = email
            send_email = EmailMessage(mail_subject,message,to=[to_email])
            send_email.send()  
            messages.success(request,"Password reset has been send to your email address")
            return redirect("login")
        else:
             messages.warning(request,"Email doesnot exists")
             return redirect("forgetpasswords")
    return render(request,"forgetpasswords.html")



def reset_password_validate(request,uidb64,token):
    try:
        uuid = urlsafe_base64_decode(uidb64).decode()
        user = User._default_manager.get(pk=uuid)
    except(TypeError,ValueError,OverflowError):
        user = None
    if user is not None and default_token_generator.check_token(user, token):
        request.session['uid'] = uuid
        messages.success(request,"Please reset your password")
        return redirect("resetpassword")
    else:
        return redirect("login")

def resetpassword(request):
    if request.method == "POST":
        password = request.POST["password"] 
        conf_password = request.POST["password2"] 
        if password == conf_password:
            uid = request.session.get('uid')
            user = User.objects.get(pk=uid)
            user.set_password(password)
            user.save()
            messages.success(request,"Your password has been successfully recovered")
            return redirect("login")

        else:
            messages.warning("Password doesnot match")
            return redirect("resetpassword")
    return render(request,"resetpassword.html")


