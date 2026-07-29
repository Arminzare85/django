from django.shortcuts import render, redirect
from django.http import HttpResponse,JsonResponse
from website.forms import ContactForm
from django.contrib import messages

def home_views(request): 
    
    context={'name':'Armin Zare' , 'text' :'I am armin zare  , im trying to learn Django , its hard but i can do this as always'}
    return render(request ,'website/index.html' , context)

def about_views(request):
    return render(request ,'website/about.html')



def contact_views(request):
    if request.method == "POST":
        form = ContactForm(request.POST)

        if form.is_valid():
            contact = form.save(commit=False)
            contact.name = "unknown"
            form.save()
            messages.success(request, "successfully posted")
            return redirect("website:contact")

    else:
        form = ContactForm()

    return render(request, "website/contact.html", {"form": form})
    

