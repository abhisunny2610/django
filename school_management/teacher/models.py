from django.db import models

# Create your models here.
class Teacher(models.Model):
    Name = models.CharField(max_length=30, default="")
    Subject = models.CharField(max_length=30, default="")
    Qualification = models.CharField(max_length=10, default="")
    City = models.CharField(max_length=15,default="", null=True)
    Contact = models.CharField(max_length=10, default="", null=True)
    Dob = models.DateField()
    Salary = models.CharField(max_length=10, null=True)
    Performance = models.CharField(default="", max_length=10, null=True)
    Image = models.ImageField(upload_to='Image', blank=True, null=True)
    Registered = models.DateField(auto_now_add=True)

    def register_student(self, Name, Subject, Qualification,Salary, Performance, City, Contact, Dob, Image, Registered):
        self.Name = Name
        self.Subject = Subject
        self.Qualification = Qualification
        self.Salary = Salary
        self.Performance = Performance
        self.City = City
        self.Contact = Contact
        self.Dob = Dob
        self.Image = Image
        self.Registered = Registered

        self.save()