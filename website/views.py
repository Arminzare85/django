from django.shortcuts import render
from django.http import HttpResponse,JsonResponse

def home_views(request):
    return render(request ,'website/home.html')

def about_views(request):
    return render(request ,'website/about.html')

def contact_views(request):
    return render(request ,'website/contact.html')

