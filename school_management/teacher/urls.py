from django.urls import path
from . import views

urlpatterns = [
    path("", view=views.teacher_home, name="teacher_home"),
    path('add_notice/', view=views.add_notice, name="add_notice"),
    path('teacher_profile/', view=views.teacher_profile, name="teacher_profile"),

    # question and answer related urls
    path("add_question/", view=views.add_question, name="add_question"),
    path("answer/", view=views.answer, name="answer"),
    path("delete_question/<int:id>", view=views.delete_question, name="delete_question"),
    path("update_question/<int:id>", view=views.update_question, name="update_question")
]
