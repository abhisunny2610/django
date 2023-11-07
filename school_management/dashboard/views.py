from django.shortcuts import render, redirect
from teacher.models import Teacher
from student.models import Student
from django.contrib.auth.models import User

# Create your views here.

# admin home view
# -----------------------------------------------------------------------------------------------
def admin_dashboard(request):
    student = Student.objects.all()
    teacher = Teacher.objects.all()
    student_length = len(student)
    teacher_length = len(teacher)

    context = {
        "Student": student,
        "Teacher": teacher ,
        "teacher_length" : teacher_length,
        "student_length": student_length
    }

    return render(request, "Admin_Dashboard.html",context)


# -----------------------------------------------------------------------------------------------
# admin students view
def admin_student(request):
    if request.method == "GET":
        student = Student.objects.all()
        return render(request, "Admin_Student.html", {"Student": student})

    if request.method == "POST":
        student = Student()

        student_user_data = student.generate_user_details(request.POST)

        if student_user_data:
            username, password = student_user_data
            user = User.objects.create_user(username=username, password=password)

            student.register_student(data=request.POST, userAccount=user, file=request.FILES)

        # return render(request, "Admin_Student.html")
    return redirect(request, "admin_student")    
    


# -----------------------------------------------------------------------------------------------
# admin teacher view
def admin_teacher(request):

    if request.method == "GET":
        teacher = Teacher.objects.all()
        # print("Teacher length", len(teacher))
        return render(request, "Admin_Teacher.html", {"Teacher": teacher})

    if request.method == "POST":
        # print(request.POST)

        teacher = Teacher()

        
        teacher_user_data = teacher.generate_user_details(request.POST)

        if teacher_user_data:
            username, password = teacher_user_data
            user =  User.objects.create_user(username=username, password=password)

            # print("username: ", username)
            # print("password: ", password)
            teacher.regitster_teacher(data=request.POST, userAccount=user,  file=request.FILES)


    return render(request, "Admin_Teacher.html")


# -----------------------------------------------------------------------------------------------
# admin notice view
def admin_notice(request):
    return render(request, "Admin_Notice.html")


# -----------------------------------------------------------------------------------------------
# admin employee view
def admin_employee(request):
    return render(request, "Admin_Employee.html")