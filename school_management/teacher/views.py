from django.shortcuts import render

# Create your views here.

# teacher home
def teacher_home(request):
    return render(request, 'Teacher_Home.html')