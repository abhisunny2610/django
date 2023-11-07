from django.shortcuts import render
from teacher.models import Teacher
from student.models import Student
from django.contrib.auth.models import User

# Create your views here.

# admin home view
def admin_dashboard(request):
    return render(request, "Admin_Dashboard.html")

# admin students view
def admin_student(request):    
    if request.method == "POST":
        student = Student()
        

# admin teacher view
def admin_teacher(request):

    if request.method == "POST":
        print(request.POST)

        teacher = Teacher()
        
        teacher_user_data = teacher.generate_user_details(request.POST)

        if teacher_user_data:
            username, password = teacher_user_data
            user =  User.objects.create_user(username=username, password=password)

            print("username: ", username)
            print("password: ", password)
            teacher.regitster_teacher(data=request.POST, userAccount=user)


    return render(request, "Admin_Teacher.html")

# admin notice view
def admin_notice(request):
    return render(request, "Admin_Notice.html")

# admin employee view
def admin_employee(request):
    return render(request, "Admin_Employee.html")