from django.urls import path
from . import views

urlpatterns = [
    path("", view=views.AddTodo, name="addTodo"),
    path("update/<int:id>/", view=views.UpdateTodo, name="updateTodo"),
    path("delete/<int:id>/", view=views.DeleteTodo, name="deleteTodo")
]