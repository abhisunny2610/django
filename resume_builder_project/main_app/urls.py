from django.urls import path
from . import views

urlpatterns = [
    path("", view=views.home, name="home"),
    path("person_form", view=views.personForm, name="personForm"),
    # path("education_form", view=views.educationForm, name="educationForm"),
    # path("experience_form", view=views.experienceForm, name="experienceForm"),
    # path("skills_form", view=views.skillsForm, name="skillsForm"),
    # path("project_form", view=views.projectForm, name="projectForm"),
    # path("template_1", view=views.template1, name="template_1"),
    # path("template_2", view=views.template2, name="template_2"),
]
