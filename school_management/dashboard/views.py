from django.shortcuts import render

# Create your views here.
def admin_dashboard(request):
    return render(request, "Admin_Dashboard.html")

def admin_student(request):
    return render(request, "Admin_Student.html")

def admin_teacher(request):
    return render(request, "Admin_Teacher.html")