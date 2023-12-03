from django.shortcuts import render, redirect
from .models import PersonDetails, EducationDeatils, ExperienceDetails, SkillsDetails, ProjectDetails
from .forms import PersonForm, EducationForm, ExerpienceForm, SkillsForm, ProjectForm

# Create your views here.




def home(request):
    return render(request, "Pages/Home.html")


def personForm(request):
    if request.method == "GET":
        person_form = PersonForm()
        edu_form = EducationForm()
        skills_form = SkillsForm()
        exp_form = ExerpienceForm()
        project_form = ProjectForm()

        context = {
            "person_form" :person_form,
            "edu_form" :edu_form,
            "skills_form" :skills_form,
            "exp_form" :exp_form,
            "project_form" :project_form,
        }

        return render(request, "Forms/Person.html", context)


    if request.method == "POST":
        person_form = PersonForm(request.POST)
        edu_form = EducationForm(request.POST)
        skills_form = SkillsForm(request.POST)
        exp_form = ExerpienceForm(request.POST)
        project_form = ProjectForm(request.POST)

        if all([form.is_valid() for form in [person_form, edu_form, skills_form, exp_form, project_form]]):
            person_form.save()
            edu_form.save()
            skills_form.save()
            exp_form.save()
            project_form.save()

            return redirect('home')
        

# def educationForm(request):
#     if request.method == "GET":
#         edu_form = EducationForm(request.POST)
#         return render(request, "Forms/Education.html", {"form": edu_form})

#     if request.method == "POST":
#         edu_form = EducationForm(request.POST)
#         if edu_form.is_valid():
#             edu_form.save()
#             return redirect("skillsForm")
        
        
# def skillsForm(request):
#     if request.method == "POST":
#         skill_form = SkillsForm(request.POST)
#         if skill_form.is_valid():
#             skill_form.save()
#             return redirect("experienceForm")
        
        
# def experienceForm(request):
#     if request.method == "POST":
#         ex_form = ExerpienceForm(request.POST)
#         if ex_form.is_valid():
#             ex_form.save()
#             return redirect("projectForm")
        
    
# def projectForm(request):
#     if request.method == "POST":
#         project_form = ProjectForm(request.POST)
#         if project_form.is_valid():
#             project_form.save()
#             return redirect("template_1")
            


def template1(request):
    if request.method == "GET":
        pass


def template2(request):
    if request.method == "GET":
        pass



