from django.contrib import admin
from .models import PersonDetails, EducationDeatils, ExperienceDetails, ProjectDetails, SkillsDetails

# Register your models here.
admin.site.register(PersonDetails)
admin.site.register(EducationDeatils)
admin.site.register(ExperienceDetails)
admin.site.register(SkillsDetails)
admin.site.register(ProjectDetails)
