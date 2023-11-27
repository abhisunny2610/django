from django.urls import path
from . import views

urlpatterns = [
    path("", view=views.home, name="home"),
    path("details_form", view=views.details_form, name="details_form")
]
