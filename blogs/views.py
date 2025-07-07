from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import AuthenticationForm


import random
from datetime import datetime, timedelta


def blogs(request):
    context = {
        "title": "Blogs",
        "random_number_from_api": random.randint(1, 100),
        "current_time": datetime.now().strftime("%d.%m.%Y %H:%M:%S"),
        "username": request.user.username if request.user.is_authenticated else "Guest",
    }
    return render(request, "blogs/blogs.html", context=context)


def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("/blogs/") 
    else:
        form = AuthenticationForm()
    return render(request, "blogs/login.html", {"form": form})


def logoff(request):
    logout(request)
    return redirect("/blogs/login/")
