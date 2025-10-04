from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

def home(request):
    # Public home page
    return render(request, "events/home.html")

@login_required
def dashboard(request):
    return render(request, "events/dashboard.html")

@login_required
def calendar(request):
    return render(request, "events/calendar.html")

def about(request):
    return render(request, "events/about.html")

def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username", "")
        password = request.POST.get("password", "")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # You could also respect ?next=... here if you want
            return redirect("dashboard")
        return render(request, "events/login.html", {"error": "Invalid username or password"})
    return render(request, "events/login.html")

def logout_view(request):
    logout(request)
    return redirect("home")