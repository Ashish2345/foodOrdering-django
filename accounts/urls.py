
from django.urls import path
from . import views

urlpatterns = [

    path("login/",views.logins,name="login"),
    path("register/",views.register,name="register"),
    path("logoutUser/",views.logoutUser,name="logoutUser"),
    path("activate/<uidb64>/<token>",views.activate,name="activate"),
    path("dashboard/",views.dashboard,name="dashboard"),
    path("forgetpasswords/",views.forgetpasswords,name="forgetpasswords"),
    path("reset-password-validate/<uidb64>/<token>",views.reset_password_validate,name="reset-password-validate"),
    path("resetpassword/",views.resetpassword,name="resetpassword"),


]