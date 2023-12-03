from django.db import models

# Create your models here.

# class YearOnlyField(models.DateField):
#     def __init__(self, *args, **kwargs):
#         kwargs['input_formats'] = ['%Y']
#         super().__init__(*args, **kwargs)


class PersonDetails(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    profession = models.CharField(max_length=50)
    profile = models.TextField()
    contact = models.CharField(max_length=10)
    email = models.EmailField()
    city = models.CharField(max_length=30)
    github = models.URLField(blank=True, null=True)
    linkedin = models.URLField(blank=True, null=True)

    def fullname(self):
        return " ".join([self.first_name, self.last_name])

    def __str__(self):
        return self.first_name + self.last_name
    


class EducationDeatils(models.Model):
    person = models.ForeignKey(PersonDetails, on_delete=models.CASCADE)
    education_1 = models.CharField(max_length=30)
    education_1_college = models.CharField(max_length=50)
    education_1_start = models.CharField(max_length=30,null=True, blank=True)
    education_1_end= models.CharField(max_length=30,blank=True, null=True)
    education_1_description = models.TextField(null=True, blank=True)

    education_2 = models.CharField(max_length=30, blank=True, null=True)
    education_2_college = models.CharField(max_length=50, blank=True, null=True)
    education_2_start = models.CharField(max_length=30,blank=True, null=True)
    education_2_end= models.CharField(max_length=30,blank=True, null=True)
    education_2_description = models.TextField(null=True ,blank=True)

    def educ_duraction_1(self):
        return " - ".join([self.education_1_start, self.education_1_end])

    def educ_duraction_2(self):
        return " - ".join([self.education_2_start, self.education_2_end])
    

class SkillsDetails(models.Model):
    person = models.ForeignKey(PersonDetails, on_delete=models.CASCADE)
    skill_1 = models.CharField(max_length=20)
    skill_2 = models.CharField(max_length=20)
    skill_3 = models.CharField(max_length=20)
    skill_4 = models.CharField(max_length=30, blank=True, null=True)
    skill_5 = models.CharField(max_length=30, blank=True, null=True)


class ProjectDetails(models.Model):
    person = models.ForeignKey(PersonDetails, on_delete=models.CASCADE)
    project_1 = models.CharField(max_length=50)
    project_1_url = models.URLField(blank=True, null=True)
    project_1_desc = models.TextField(blank=True, null=True)

    project_2 = models.CharField(max_length=50)
    project_2_url = models.URLField(blank=True, null=True)
    project_2_desc = models.TextField(blank=True, null=True)


class ExperienceDetails(models.Model):
    person = models.ForeignKey(PersonDetails, on_delete=models.CASCADE)
    experience_1 = models.CharField(max_length=30)
    experience_1_company = models.CharField(max_length=50)
    experience_1_start = models.CharField(max_length=30,blank=True, null=True)
    experience_1_end= models.CharField(max_length=30,blank=True, null=True)
    experience_1_description = models.TextField(null=True, blank=True)

    experience_2 = models.CharField(max_length=30, blank=True, null=True)
    experience_2_company = models.CharField(max_length=50, blank=True, null=True)
    experience_2_start = models.CharField(max_length=30,blank=True, null=True)
    experience_2_end= models.CharField(max_length=30,blank=True, null=True)
    experience_2_description = models.TextField(null=True ,blank=True)

    def ex_duraction_1(self):
        return " - ".join([self.experience_1_start, self.experience_1_])
    
    def ex_duraction_2(self):
        return " - ".join([self.experience_2_start, self.experience_2_end])


 


    

    



