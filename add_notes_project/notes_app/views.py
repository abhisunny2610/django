from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.models import User, Permission
from django.http import HttpResponse
from .models import Notes

# Create your views here.

# -----------------------------------------------------------------------------------------------


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


# -----------------------------------------------------------------------------------------------
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


# -------------------------------------------------------------------------------------------------
def logout(request):
    if request.method == "GET":
        auth.logout(request)

    return redirect("login")


# -------------------------------------------------------------------------------------------------
def home(request):
    if request.user.is_authenticated:
        notes = Notes.objects.filter(user_id=request.user.id)
        return render(request, "Pages/Home.html", {"notes": notes})
    else:
        return redirect("login")


# -------------------------------------------------------------------------------------------------
def addnote(request):
    if request.method == "GET":
        return render(request, "Home.html")

    if request.method == "POST" and request.user.is_authenticated:
        title = request.POST.get("title")
        description = request.POST.get("description")

        notes = Notes()
        notes.title = title
        notes.description = description
        notes.user = request.user
        notes.save()

        return redirect("home")


# -------------------------------------------------------------------------------------------------
def delete(request, id):
    if request.method == 'GET' and request.user.is_authenticated:
        note = Notes.objects.get(pk=id)
        note.delete()
        return redirect("home")


# -------------------------------------------------------------------------------------------------
def update(request, id):
    if request.method == "GET":
        note = Notes.objects.get(pk=id)
        return render(request, "Pages/Home.html", {"note": note})

    if request.method == "POST" and request.user.is_authenticated:
        title = request.POST.get("title")
        description = request.POST.get("description")
        note = Notes.objects.get(pk=id)

        note.title = title
        note.description = description
        note.save()

        return redirect("home")
