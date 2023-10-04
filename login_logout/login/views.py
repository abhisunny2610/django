from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import auth

# Create your views here.

def home(request):
    if (request.user.is_authenticated):
        return render(request, "Todo.html")

    return redirect("signin")

def signup(request):
    if request.method == "GET":
        return render(request, "signup.html")
    
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get('password')
        cpassword = request.POST.get('cpassword')

        if (password == cpassword):
            user = User.objects.create_user(username, email, password)

            user.save()

            return redirect("signin")
        return HttpResponse("Password Mismatch...")
    
def signin(request):
    if request.method == "GET":

        if not request.user.is_authenticated:
            return render(request, "login.html")
        
        return redirect("home")
    
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        _user = auth.authenticate(request, username=username, password = password)

        if _user:
            auth.login(request, _user)
            return redirect("todo_home")
        else:
            return HttpResponse("Username or password in incorrect")
    
def logout(request):
    if request.method == "GET":
        auth.logout(request)

    return redirect("signin")
