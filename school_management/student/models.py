from django.db import models
from django.contrib.auth.models import User

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
    userAccount = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    def register_student(self, data, userAccount):
        self.Name = data.get("name")
        self.Std = data.get("class")
        self.Father_name = data.get("parent-name")
        self.Contact = data.get("contact") 
        self.Dob = data.get("dob")

        self.userAccount = userAccount 
        self.userAccount.save()

        self.save()

    def generate_user_details(self, data):
        userName= data.get("name")
        userdob = data.get("dob")

        if (len(userName) == 0) and (len(userdob) == 0):
            return False
        
        userdob_ = ''.join(userdob.split('-'))
        return (userName, userName.upper()+'@'+userdob_)

    
