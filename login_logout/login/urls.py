from django.urls import path
from . import views

urlpatterns = [
    path("", view=views.home, name="home"),
    path("signup", view=views.signup, name="signup"),
    path("signin", view=views.signin, name="signin"),
    path("logout/", view=views.logout, name="logout")
]
