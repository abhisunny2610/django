from django.urls import path
from . import views

urlpatterns = [
    path("", view=views.student_home, name="student_home")
]

