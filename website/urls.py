from django.contrib import admin
from django.urls import path , include
from website.views import *

app_name =  'website'

urlpatterns = [
    
    path("",home_views,name="index"),
    path("about",about_views,name="about"),
    path("contact",contact_views,name="contact")   
]