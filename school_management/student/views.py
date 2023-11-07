from django.shortcuts import render

# Create your views here.
# -----------------------------------------------------------------------------------------------
def student_home(request):
    return render(request, "Student/Student_home.html")