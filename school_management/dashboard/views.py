from django.shortcuts import render, redirect
from teacher.models import Teacher
from student.models import Student
from .models import Employee, Notice
from django.contrib.auth.models import User

# Create your views here.

# admin home view
# -----------------------------------------------------------------------------------------------
def admin_dashboard(request):
    student = Student.objects.all()
    teacher = Teacher.objects.all()
    employee = Employee.objects.all()
    notice = Notice.objects.all()
    student_length = len(student)
    teacher_length = len(teacher)
    employee_length = len(employee)
    notice_length = len(notice)

    context = {
        "Student": student,
        "Teacher": teacher,
        "Employee": employee,
        "Notice": notice,
        "teacher_length": teacher_length,
        "student_length": student_length,
        "employee_length": employee_length,
        "notice_length": notice_length,

    }

    return render(request, "Admin_Dashboard.html", context)


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
            user = User.objects.create_user(
                username=username, password=password)

            student.register_student(
                data=request.POST, userAccount=user, file=request.FILES)

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
            user = User.objects.create_user(
                username=username, password=password)

            # print("username: ", username)
            # print("password: ", password)
            teacher.regitster_teacher(
                data=request.POST, userAccount=user,  file=request.FILES)

    return render(request, "Admin_Teacher.html")


# -----------------------------------------------------------------------------------------------
# admin notice view
def admin_notice(request):
    if request.method == "GET":
        notice = Notice.objects.all()
        return render(request, "Admin_Notice.html", {"Notice": notice})

    if request.method == "POST":
        notice = Notice()
        notice.register_notice(request.POST)
        return redirect("admin_notice")


# -----------------------------------------------------------------------------------------------
# admin employee view
def admin_employee(request):
    if request.method == "GET":
        employee = Employee.objects.all()
        return render(request, "Admin_Employee.html", {"Employee": employee})

    if request.method == "POST":
        employee = Employee()
        employee.register_employee(request.POST)
        return redirect("admin_employee")


# -----------------------------------------------------------------------------------------------
def delete_teacher(request, id):
    if request.method == "GET":
        teacher = Teacher.objects.get(pk=id)
        teacher.delete()
        return redirect("admin_dashboard")
    

# -----------------------------------------------------------------------------------------------
def delete_student(request, id):
    if request.method == "GET":
        student = Student.objects.get(pk=id)
        student.delete()
        return redirect("admin_dashboard")
    

# -----------------------------------------------------------------------------------------------
def delete_employee(request, id):
    if request.method == "GET":
        employee = Employee.objects.get(pk=id)
        employee.delete()
        return redirect("admin_employee")