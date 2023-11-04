from django.shortcuts import render

# Create your views here.
def login(request):
    return render(request, "Account/login.html")

def signup(request):
    return render(request, "Account/Register.html")