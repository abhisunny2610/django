from django.urls import path
from . import views

urlpatterns = [
    path("", view=views.student_home, name="student_home"),
    path("logout/", view=views.student_logout, name="student_logout")
]

