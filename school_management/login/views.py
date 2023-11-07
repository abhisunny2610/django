from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.models import User

from student.models import Student
from teacher.models import Teacher


# Create your views here.

# -----------------------------------------------------------------------------------------------
def login_as_student(request, username, password):
    # print("logging as student...")
    user = auth.authenticate(request=request, username=username, password=password)
    if user:
        student = Student.objects.get(userAccount_id = user.id)
        return user,student


# -----------------------------------------------------------------------------------------------
def login_as_teacher(request, username, password):
    # print("logging as teacher...")
    user = auth.authenticate(request=request, username=username, password=password)
    if user:
        teacher = Teacher.objects.get(userAccount_id = user.id)
        return user,teacher
    

# -----------------------------------------------------------------------------------------------
# login view
def login(request):
    if request.method == "GET":
        return render(request, "login.html")
    
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user_type = request.POST.get("user_type")

        # print("username :", username)
        # print("password :", password)
        # print("user_type :", user_type)

        if user_type == "student":
            user,student = login_as_student(request, username, password)
            if user and student:
                request.session["userId"] = user.id
                request.session["user_type"] = "student"
                request.session["studentId"] = student.id
                auth.login(request, user)
                return redirect("student_home")
        
        if user_type == "teacher":
            user, teacher = login_as_teacher(request, username, password)
            if user and teacher:
                request.session["userId"] = user.id
                request.session["user_type"] = "teacher"
                request.session["teacherId"] = teacher.id
                auth.login(request, user)
                return  redirect("teacher_home")

    return redirect("login")
    

# -----------------------------------------------------------------------------------------------
# signup view
def signup(request):
    return render(request, "signup.html")
