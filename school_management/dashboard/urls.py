from django.urls import path
from . import views

urlpatterns = [
    path("", view=views.admin_dashboard, name="admin_dashboard"),
    path("admin_student/", view=views.admin_student, name="admin_student"),
    path("admin_teacher", view=views.admin_teacher, name="admin_teacher")
]
