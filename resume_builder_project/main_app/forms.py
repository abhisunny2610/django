from django import forms
from .models import PersonDetails, ExperienceDetails, EducationDeatils, ProjectDetails, SkillsDetails

# validators=[RegexValidator(regex='^(\+?\d{1,3})?[-.\s]?\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}$')]


class PersonForm(forms.ModelForm):
    class Meta:
        model = PersonDetails
        fields = ('first_name', "last_name", "profession", "profile",
                  "contact", "email", "city", "github", "linkedin")
        

class EducationForm(forms.ModelForm):
    class Meta:
        model = EducationDeatils
        fields = ('education_1','education_1_college','education_1_start','education_1_end','education_1_description', 'education_2','education_2_college','education_2_start','education_2_end','education_2_description')

class SkillsForm(forms.ModelForm):
    class Meta:
        model = SkillsDetails
        fields = ('skill_1', 'skill_2', 'skill_3', "skill_4", "skill_5")


class ExerpienceForm(forms.ModelForm):
    class Meta:
        model = ExperienceDetails
        fields= ('experience_1','experience_1_company','experience_1_start','experience_1_end','experience_1_description', 'experience_2','experience_2_company','experience_2_start','experience_2_end','experience_2_description')


class ProjectForm(forms.ModelForm):
    class Meta:
        model = ProjectDetails
        fields = ('project_1','project_1_url','project_1_desc')
