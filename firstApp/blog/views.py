from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import MyUser
from django.contrib.auth.models import User
from django.contrib import auth
from .models import TodoList

# Create your views here.
def home(request):
    
    if (request.user.is_authenticated):
        return render(request, "index.html")
    
    return redirect("login")

def addEntry(request):
    if request.method == "GET":
        print("Sending add entry template...")
        return render(request, "addEntry.html")
    
    if request.method == "POST":
        print("processing add entry data")
        user = MyUser()

        user.firstName = request.POST.get("firstName")
        user.lastName = request.POST.get("lastName")
        user.email = request.POST.get("email")

        user.save()

        return HttpResponse("Request Submitted...")


# def welcome(request):

#     web_details = {
#         "name": "Faltu Website",
#         "founder": "Seema Haider",
#         "living_in": "Pakistan se baagh ke india me rhe rhi he",
#         "husband": "Sachin Chaudhary"
#     }

#     return render(request, "login.html", web_details)

def login(request):
    if request.method == "GET":

        if not request.user.is_authenticated:
            return render(request, "login.html")   
        
        return redirect("home")
    
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        _user = auth.authenticate(request, username = username, password = password)

        if _user:
            auth.login(request, _user)
            return redirect("home")
        else:
            return HttpResponse("Username or password in incorrect")
        
def logout(request):
    if request.method == "GET":
        auth.logout(request)

    return redirect("login")


def registration(request):
    if request.method == "GET":
        return render(request, "registration.html")   
    
    if request.method == "POST":
        username = request.POST.get("username")
        firstname = request.POST.get("firstName")
        lastname = request.POST.get("lastName")
        email = request.POST.get("email")
        password = request.POST.get("password")
        cpassword = request.POST.get("cpassword")

        if (password == cpassword):
            user = User.objects.create_user(username, email, password, first_name= firstname, last_name= lastname)

            user.save()

            return HttpResponse("Request Submitted...")

        return HttpResponse("Password Mismatch")
    
def AddTodo(request):
    if request.method == "GET":
        todos = TodoList.objects.all()
        return render(request, "TodoList.html", {"todos": todos})
    

    if request.method == "POST":
        content = request.POST.get("todocontent")

        todo = TodoList()
        todo.isCompleted = False
        todo.content = content
        todo.save()
        return render(request, "TodoList.html")