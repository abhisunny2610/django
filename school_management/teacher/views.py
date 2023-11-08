from django.shortcuts import render, redirect
from .models import Teacher, AddQuestion
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
    teacher_id = request.session.get("teacherId")
    teacher = Teacher.objects.get(pk=int(teacher_id))
    student = Student.objects.all()

    context = {
        "Teacher": teacher,
        "Student": student,

    }
    return render(request, "Admin_Notice.html",context)


# -----------------------------------------------------------------------------------------------
def teacher_profile(request):
    pass


# -----------------------------------------------------------------------------------------------
def answer(request):
    if request.method == "GET":
        teacher_id = request.session.get("teacherId")
        teacher = Teacher.objects.get(pk=int(teacher_id))
        question = AddQuestion.objects.all()

        context = {
            "Teacher": teacher,
            "Question":question
        }
        return render(request, "Teacher_answer.html", context)


# -----------------------------------------------------------------------------------------------
def add_question(request):
    if request.method == "GET":
        teacher_id = request.session.get("teacherId")
        teacher = Teacher.objects.get(pk=int(teacher_id))
        student = Student.objects.all()

        context = {
            "Teacher": teacher,
            "Student": student,

        }
        return render(request, "Teacher_Add_Question.html", context)
    
    if request.method == "POST":
        question = AddQuestion()
        question.add_question(request.POST)

        return redirect("add_question")


# -----------------------------------------------------------------------------------------------
def delete_question(request , id):
    if request.method == "GET":
        question = AddQuestion.objects.get(pk=id)
        question.delete()
        return redirect("answer")
    

# -----------------------------------------------------------------------------------------------
def update_question(request, id):
    if request.method == "GET":
        pass

    if request.method == "POST":
        pass

