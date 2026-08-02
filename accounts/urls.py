from django.contrib import admin
from django.urls import path , include
from accounts.views import *
from django.contrib.auth import views as auth_views


app_name =  'accounts'

urlpatterns = [
    path("login/",login_views,name="login"),
    path("logout/",logout_views,name="logout"),
    path("signup/",signup_views,name="signup"),
    path(
        "password_reset_form/",password_reset_form_views,name="password_reset_form"
    ),

   
]