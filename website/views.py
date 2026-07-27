from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from blog.models import Post

def home_views(request): 
    posts = Post.objects.filter(status=True)
    context={'name':'Armin Zare' , 'text' :'I am armin zare  , im trying to learn Django , its hard but i can do this as always',"posts": posts}
    return render(request ,'website/index.html' , context)

def about_views(request):
    return render(request ,'website/about.html')

def contact_views(request):
    return render(request ,'website/contact.html')


