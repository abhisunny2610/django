from django.urls import path
from . import views

urlpatterns = [
     path("", view=views.login, name="login"),
     path("signup/", view=views.signup, name="signup"),
     path("admin_dashboard/", view=views.dashboard_login, name="admin_dashboard")
]
