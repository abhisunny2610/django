from django.shortcuts import render, redirect
from .models import PersonDetails, EducationDeatils, ExperienceDetails, SkillsDetails, ProjectDetails
from .forms import PersonForm, EducationForm, ExerpienceForm, SkillsForm, ProjectForm

# Create your views here.


def home(request):
    return render(request, "Pages/Home.html")


def personForm(request):
    if request.method == "GET":
        person_form = PersonForm()
        return render(request, "Forms/Person.html", {"form":person_form})


    if request.method == "POST":
        person_form = PersonForm(request.POST)

        if person_form.is_valid():
            person_form.save()
            return redirect('home')
            


