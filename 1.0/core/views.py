from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm, EmailAuthenticationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash

# Landing Page
def landing_page(request):
    return render(request, "core/landing.html")

# About Page
def about_page(request):
    team = [
        {"name": "1", "bio": "BioHere.", "role": "RoleHere", "image": "images/genImage.png"},
        {"name": "2", "bio": "BioHere.", "role": "RoleHere", "image": "images/genImage.png"},
        {"name": "3", "bio": "BioHere.", "role": "RoleHere", "image": "images/genImage.png"},
        {"name": "4", "bio": "BioHere.", "role": "RoleHere", "image": "images/genImage.png"},
        {"name": "5", "bio": "BioHere.", "role": "RoleHere", "image": "images/genImage.png"},
    ]
    return render(request, "core/about.html", {"team": team})

# Registration
def register_view(request):
    if request.user.is_authenticated:
        return redirect("dashboard")

    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("dashboard")
    else:
        form = CustomUserCreationForm()

    return render(request, "core/register.html", {"form": form})

# Login
def login_view(request):
    if request.method == "POST":
        form = EmailAuthenticationForm(request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect("dashboard")
    else:
        form = EmailAuthenticationForm()

    return render(request, "core/login.html", {"form": form})

# Dashboard
@login_required
def dashboard_view(request):
    return render(request, "core/dashboard.html")

# Reset Password (Internal)
@login_required
def password_change_view(request):
    if request.method == "POST":
        form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  
            return redirect("dashboard")
    else:
        form = PasswordChangeForm(user=request.user)

    return render(request, "core/reset_password.html", {"form": form})
