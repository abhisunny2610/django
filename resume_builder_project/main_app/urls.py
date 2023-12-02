from django.urls import path
from . import views

urlpatterns = [
    path("", view=views.home, name="home"),
    path("person_form", view=views.personForm, name="person_form")
]
