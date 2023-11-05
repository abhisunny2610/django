from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.models import User, Permission
from django.http import HttpResponse

# Create your views here.

#-----------------------------------------------------------------------------------------------
def login(request):
    if request.method == "GET":
        if not request.user.is_authenticated:    
            return render(request, "Account/login.html")
        return redirect("home")
    
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = auth.authenticate(request, username=username, password=password)

        if user:
            auth.login(request, user)
            return redirect("home")
        else:
            return HttpResponse("Username or Password incorrect.")
        

#-----------------------------------------------------------------------------------------------
def signup(request):
    if request.method == "GET":
        return render(request, "Account/Register.html")
    
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        cpassword = request.POST.get("cpassword")

        if (password == cpassword):
            user = User.objects.create_user(username, email, password)
            user.save()

            return redirect("login")
        

#-------------------------------------------------------------------------------------------------
def home(request):
    return render(request, "Pages/Home.html")


#-------------------------------------------------------------------------------------------------
def logout(request):
    if request.method == "GET":
        auth.logout(request)

    return redirect("login")


#-------------------------------------------------------------------------------------------------
def addnote(request):
    pass