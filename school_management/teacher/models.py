from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Teacher(models.Model):
    Name = models.CharField(max_length=30, default="")
    Subject = models.CharField(max_length=30, default="")
    Qualification = models.CharField(max_length=10, default="")
    City = models.CharField(max_length=15,default="", null=True)
    Contact = models.CharField(max_length=10, default="", null=True)
    Dob = models.DateField()
    Salary = models.CharField(max_length=10, null=True)
    Performance = models.CharField(default="Good", max_length=10,)
    Image = models.ImageField(upload_to='Image', blank=True, null=True)
    Registered = models.DateField(auto_now_add=True)
    userAccount = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    def regitster_teacher(self, data, userAccount, file):
        self.Name = data.get("name")
        self.Subject = data.get("subject")
        self.Qualification = data.get("qualification")
        self.Salary = data.get("salary")
        self.Contact = data.get("contact")
        self.Dob = data.get("dob")
        self.Image = file.get("image")
        self.City = data.get("city")
        

        self.userAccount = userAccount
        # first save the user account
        self.userAccount.save()

        # then save the account.
        self.save()



    def generate_user_details(self, data):

        userName = data.get("name")
        userdob = data.get("dob")

        if len(userName) == 0:
            return False 
        
        if len(userdob) == 0:
            return False
        
        # generating the password.
        userdob_ = "".join(userdob.split('-'))
        return (userName, userName.upper() + "@" + userdob_)

    
    def __str__(self):
        return self.Name

