from django.urls import path
from . import views
urlpatterns = [
     path("", view=views.todo_home, name="todo_home"), # todo
    path("addTodo/", view=views.addTodo, name="addTodo"),
    path("deleteTodo/<int:id>/", view=views.deleteTodo, name="deleteTodo"),
    path("updateTodo/<int:id>", view=views.updateTodo, name="updateTodo")
]
