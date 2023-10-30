from django.shortcuts import render
from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import Images

# Create your views here.
def home(request):
    return render(request, "Home.html", )

def about(request):
    return render(request, "About.html")

def gallery(request):
    return render(request, "Gallery.html")

def add_user(request):
    if request.method == "GET":
        return render(request, "Home.html")
    
    if request.method == "POST":
        name = request.POST.get("username")
        image  = request.FILES.get("userimage")

        images = Images()
        images.insertDeatils(name, image)
        return redirect("Home.html")