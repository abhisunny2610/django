from django.shortcuts import render, redirect
from .models import Student
from teacher.models import AddQuestion
from django.contrib import auth

# Create your views here.
# -----------------------------------------------------------------------------------------------
def student_home(request):
    student_id = request.session.get("studentId")
    student = Student.objects.get(pk=int(student_id))
    question = AddQuestion.objects.all()
    return render(request, "Student/Student_home.html", {"Student": student, "Question":question})

def student_logout(request):
    if request.method == "GET":
        auth.logout(request)

    return redirect("login")