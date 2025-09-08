from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import AuthenticationForm

# from models import User
# from forms import UserLoginForm
from .forms import LoginForm, ProfileForm


from datetime import datetime, timedelta

# def home(request):
#     context = {
#         "title": "Home",
#         "current_time": datetime.now().strftime("%d.%m.%Y %H:%M:%S"),
#         "username": request.user.username if request.user.is_authenticated else "Guest",
#     }
#     return render(request, "blogs/home.html", context=context)

def blogs(request):
    context = {
        "title": "Blogs",
        "current_time": datetime.now().strftime("%d.%m.%Y %H:%M:%S"),
        "username": request.user.username if request.user.is_authenticated else "Guest",
    }
    return render(request, "blogs/blogs.html", context=context)

def logoff(request):
    logout(request)
    return redirect("/blogs/")

def login_view(request):
    if request.method == "POST":
        # form = AuthenticationForm(request, data=request.POST)
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("/blogs/") 
        
    else:
        # form = AuthenticationForm()
        form = LoginForm()
    # return render(request, "blogs/login.html", {"form": form})
    return render(request, "blogs/login.html", {"form": form})

def profile_edit(request):
    profile = request.user.profile
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = ProfileForm(instance=profile)
    return render(request, 'blogs/profile_edit.html', {'form': form})

