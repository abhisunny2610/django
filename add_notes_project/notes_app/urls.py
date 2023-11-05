from django.urls import path
from . import views

urlpatterns = [
    # ---------------- Account Urls -----------------------
    path("", view=views.login, name="login"),
    path("signup/", view=views.signup, name="signup"),
    path("logout/", view=views.logout, name="logout"),

    # ---------------- App Urls -----------------------
    path("home/", view=views.home, name="home"),
    path("addnote/", view=views.addnote, name="addnote")
]
