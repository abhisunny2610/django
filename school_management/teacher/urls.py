from django.urls import path
from . import views

urlpatterns = [
    path("", view=views.teacher_home, name="teacher_home"),
    path("answer/", view=views.answer, name="answer"),
    path("add_question/", view=views.add_question, name="add_question"),
    path('add_notice/', view=views.add_notice, name="add_notice"),
    path('teacher_profile/', view=views.teacher_profile, name="teacher_profile")
]
