from django.shortcuts import render , redirect
from django.contrib.auth import authenticate, login , logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm , UserCreationForm
from django.contrib.auth.decorators import login_required
def login_views(request):
    if request.user.is_authenticated:
        return redirect('website:index')
    else:
        if request.method == 'POST':
            form = AuthenticationForm(request.POST, data=request.POST)
            if form.is_valid():
                username = request.POST.get('username') 
                password = request.POST.get('password')
                user = authenticate(username=username, password=password)
                if user is not None:
                    login(request, user)
                    return redirect('website:index')
                else:
                    messages.error(request, "Invalid username or password")
                    return redirect('accounts:login')

            
    form = AuthenticationForm()
    context = {'form': form}
    return render(request, 'accounts/login.html', context)
@login_required
def logout_views(request):
    logout(request)
    return redirect('website:index')


def signup_views(request):

    if request.user.is_authenticated:
        return redirect("website:index")

    if request.method == "POST":
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, "Successfully created user.")
            return redirect("accounts:login")

        messages.error(request, "Please correct the errors below.")

    else:
        form = UserCreationForm()

    return render(request, "accounts/signup.html", {"form": form})
        
        