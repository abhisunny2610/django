from django.shortcuts import render

# Create your views here.

# login view
def login(request):
    return render(request, "login.html")

# signup view
def signup(request):
    return render(request, "signup.html")
