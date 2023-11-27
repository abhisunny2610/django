from django.shortcuts import render
from .forms import PersonDetailsForm

# Create your views here.


def home(request):
    return render(request, "Pages/Home.html")


def details_form(request):
    form = PersonDetailsForm()
    if request.method == "GET":
        return render(request, "Forms/Details_Form.html", {"form": form})

    if request.method == "POST":
        pass
