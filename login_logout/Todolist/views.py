from django.shortcuts import render, redirect
from .models import Todos
# Create your views here.
from .utility import getPermission


def jsBool(str):
    if str == 'true':
        return True
    elif str == "false":
        return False
    return True


def todo_home(request):

    if request.user.is_authenticated:
        permission = getPermission(request.user, "Todolist", "todos")
        todos = Todos.objects.filter(user_id=request.user.id)
        print(f"User Permission: {request.user.username}", permission)
        # collecting all todos
        return render(request, "Todo.html", {"todos": todos, "permission": permission})
    else:
        return redirect("signin")


def addTodo(request):
    if request.method == "GET":
        permission = getPermission(request.user, "Todolist", "todos")
        todos = Todos.objects.filter(user_id=request.user.id)
        # collecting all todos
        print("User Permission: ", permission)
        return render(request, "Todo.html", {"todos": todos, "permission": permission})

    if request.method == "POST" and request.user.is_authenticated:

        permission = getPermission(request.user, "Todolist", "Todos")

        if permission.get("add"):
            content = request.POST.get("content")
            todo = Todos()
            todo.content = content
            todo.user = request.user
            todo.save()

        return redirect("addTodo")


def deleteTodo(request, id):
    if request.method == "GET":
        item = Todos.objects.get(pk=id)
        item.delete()
        return redirect("addTodo")


def updateTodo(request, id):
    if request.method == "GET":
        item = Todos.objects.get(pk=id)
        return render(request, "updateTodo.html", {"item": item})

    if request.method == "POST":
        content = request.POST.get("content")
        isCompleted = request.POST.get("isCompleted")
        item = Todos.objects.get(pk=id)

        if content:
            item.content = content

        if isCompleted:
            item.isCompleted = jsBool(isCompleted)
        item.save()

    return redirect("addTodo")
