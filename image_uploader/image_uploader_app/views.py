from django.shortcuts import render, redirect
from .models import Images

# Create your views here.
def home(request):
    if request.method == "GET":
        images = Images.objects.all()
        return render(request, "Home.html", {"images": images})
    
    if request.method == "POST":
        name = request.POST.get("img_name")
        img = request.FILES.get("img")

        images = Images()
        images.insertdata(name, img)
        return redirect("home")
