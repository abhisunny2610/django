from django.shortcuts import render

# Create your views here.

# admin home view
def admin_dashboard(request):
    return render(request, "Admin_Dashboard.html")

# admin students view
def admin_student(request):
    return render(request, "Admin_Student.html")

# admin teacher view
def admin_teacher(request):
    return render(request, "Admin_Teacher.html")

# admin notice view
def admin_notice(request):
    return render(request, "Admin_Notice.html")

# admin employee view
def admin_employee(request):
    return render(request, "Admin_Employee.html")