from django.urls import path
from . import views

urlpatterns = [
    path("", view=views.teacher_home, name="teacher_home")
]
