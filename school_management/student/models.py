from django.db import models

# Create your models here.
class Student(models.Model):
    Name = models.CharField(max_length=30, default="")
    Std = models.CharField(max_length=5, default="")
    Father_name = models.CharField(max_length=30, default="")
    City = models.CharField(max_length=15,default="", null=True)
    Contact = models.CharField(max_length=10, default="", null=True)
    Dob = models.DateField()
    Image = models.ImageField(upload_to='Image', blank=True, null=True)
    Registered = models.DateField(auto_now_add=True)

    def register_student(self, Name, Std, Father_name, City, Contact, Dob, Image, Registered):
        self.Name = Name
        self.Std = Std
        self.Father_name = Father_name
        self.City = City
        self.Contact = Contact
        self.Dob = Dob
        self.Image = Image
        self.Registered = Registered

        self.save()

    
