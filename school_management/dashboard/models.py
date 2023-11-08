from django.db import models

# Create your models here.
class Employee(models.Model):
    name = models.CharField(max_length=30, null=True, default="")
    parent_name = models.CharField(max_length=30, null=True, default="")
    city = models.CharField(max_length=20, null=True, default="Jaipur")
    salary = models.CharField(max_length=6, null=True, default="")
    role = models.CharField(max_length=10, null=True, default="")
    registered = models.DateField(auto_now_add=True)
    contact = models.CharField(max_length=10, default="", null=True)

    def __str__(self):
        return self.name
    
    def register_employee(self, data):
        self.name = data.get("name")
        self.parent_name = data.get("parent-name")
        self.city = data.get("city")
        self.salary = data.get("salary")
        self.role = data.get("role")
        self.contact = data.get("contact")

        self.save()