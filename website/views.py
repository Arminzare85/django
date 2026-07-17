from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse,JsonResponse

def home_views(request):
    return HttpResponse('<h1>Hello</h1>')

def about_views(request):
    return JsonResponse({'about':'view'})

def contact_views(request):
    return HttpResponse("contact")

