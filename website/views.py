from django.shortcuts import render
from django.http import HttpResponse,JsonResponse

def home_views(request):
    context={'name':'Armin Zare' , 'text' :'I am armin zare  , im trying to learn Django , its hard but i can do this as always'}
    return render(request ,'website/index.html' , context)

def about_views(request):
    return render(request ,'website/about.html')

def contact_views(request):
    return render(request ,'website/contact.html')

