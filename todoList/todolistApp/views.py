from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Todos

# Create your views here.
def AddTodo(request):
    todos = Todos.objects.all()
    if request.method == "GET":
        return render(request, "TodoList.html", {"todos": todos})
    
    if request.method == "POST":
        content = request.POST.get("todoInput")

        todo = Todos()
        todo.content = content
        todo.isCompleted = False
        todo.save()


        return redirect("addTodo")

def UpdateTodo(request, id):
    if request.method == "GET":
        item = Todos.objects.get(pk=id)
        return render(request, "UpdateList.html", {"item": item})
    
    if request.method == "POST":
        content = request.POST.get("todoInput")
        isCompleted = request.POST.get("isCompleted")
        item = Todos.objects.get(pk=id)
        item.content = content
        item.save()

        return redirect("addTodo")
    
def DeleteTodo(request, id):
    if request.method == "GET":
        item = Todos.objects.get(pk=id)
        item.delete()
        return redirect("addTodo")