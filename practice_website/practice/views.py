from django.shortcuts import render
from django.shortcuts import redirect, render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, "Home.html", )

def about(request):
    return render(request, "About.html")

def gallery(request):
    return render(request, "Gallery.html")
