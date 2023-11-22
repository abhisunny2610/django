from django.urls import path
from . import views

urlpatterns = [
    path("", view=views.admin_dashboard, name="admin_dashboard"),
    path("admin_student/", view=views.admin_student, name="admin_student"),
    path("admin_teacher", view=views.admin_teacher, name="admin_teacher"),
    path("admin_notice/", view=views.admin_notice, name="admin_notice"),
    path("admin_employee/", view=views.admin_employee, name="admin_employee"),

    # delete urls
    path("delete_teacher/<int:id>", view=views.delete_teacher, name="delete_teacher"),
    path("delete_student/<int:id>", view=views.delete_student, name="delete_student"),
    path("delete_employee/<int:id>", view=views.delete_employee, name="delete_employee"),

    # update urls
    path('update_teacher/<int:id>', view=views.update_teacher, name="update_teacher"),
    path('update_employee/<int:id>', view=views.update_employee, name="update_employee"),
    path('update_student/<int:id>', view=views.update_student, name="update_student"),

    # view urls
    path('view_student/<int:id>', view=views.view_student, name="view_student"),
    path('view_teacher/<int:id>', view=views.view_teacher, name="view_teacher"),
    path('view_employee/<int:id>', view=views.view_employee, name="view_employee"),
]
