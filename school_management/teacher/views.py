from django.shortcuts import render

# Create your views here.

# teacher home
def teacher_home(request):
    return render(request, 'Teacher_Home.html')

def add_notice(request):
    return render(request, "Admin_Notice.html")

def teacher_profile(request):
    pass

def answer(request):
    return render(request, "Teacher_answer.html")

def add_question(request):
    return render(request, "Teacher_Add_Question.html")