from django.shortcuts import render
from .models import Teacher
from student.models import Student
# Create your views here.

# -----------------------------------------------------------------------------------------------
# teacher home
def teacher_home(request):
    teacher_id = request.session.get("teacherId")
    teacher = Teacher.objects.get(pk=int(teacher_id))
    student = Student.objects.all()


    context = {
        "Teacher": teacher,
        "Student": student,

    }

    return render(request, 'Teacher_Home.html', context)


# -----------------------------------------------------------------------------------------------
def add_notice(request):
    return render(request, "Admin_Notice.html")


# -----------------------------------------------------------------------------------------------
def teacher_profile(request):
    pass


# -----------------------------------------------------------------------------------------------
def answer(request):
    return render(request, "Teacher_answer.html")


# -----------------------------------------------------------------------------------------------
def add_question(request):
    return render(request, "Teacher_Add_Question.html")
