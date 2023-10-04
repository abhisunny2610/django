from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def Home(request):
    return HttpResponse("<h1>Hello Car Dekho</h1>")