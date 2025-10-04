from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from .models import Event

# --- Default landing page ---
def home(request):
    if request.user.is_authenticated:
        return redirect("dashboard")
    return redirect("signup")

# --- Signup page ---
def signup_view(request):
    if request.user.is_authenticated:
        return redirect("dashboard")
    
    form = UserCreationForm()
    
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("dashboard")
        
    return render(request, "events/signup.html", {"form": form})

# --- Dashboard (auth required) ---
@login_required
def dashboard(request):
    return render(request, "events/dashboard.html")

# Calendar (auth required)
@login_required
def calendar(request):
    return render(request, "events/calendar.html")

# About page
def about(request):
    return render(request, "events/about.html")

def login_view(request):
    if request.user.is_authenticated:
        return redirect("dashboard")
    
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("dashboard")
        return render(request, "events/login.html", {"error": "Invalid username or password"})
    return render(request, "events/login.html")

# Logout
def logout_view(request):
    logout(request)
    return redirect("home")