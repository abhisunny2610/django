from django.shortcuts import render, redirect
from .models import Student
from django.contrib import auth

# Create your views here.
# -----------------------------------------------------------------------------------------------
def student_home(request):
    student_id = request.session.get("studentId")
    student = Student.objects.get(pk=int(student_id))
    return render(request, "Student/Student_home.html", {"Student": student})

def student_logout(request):
    if request.method == "GET":
        auth.logout(request)

    return redirect("login")