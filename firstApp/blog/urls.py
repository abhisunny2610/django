from django.urls import path
from . import views

urlpatterns = [
    path("", view = views.home, name="home"),
    path("welcome/", view=views.welcome, name="welcome"),
    path("login/", view = views.login, name="login"),
    path("addEntry/", view = views.addEntry, name="addEntry"),
    path("registration/", view= views.registration, name="registration"),
    path("logout/", view= views.logout, name="logout"),
    path("todolist/", view= views.AddTodo, name="todolist")
]