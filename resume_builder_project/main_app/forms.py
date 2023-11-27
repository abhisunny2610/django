from django import forms

# validators=[RegexValidator(regex='^(\+?\d{1,3})?[-.\s]?\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}$')]


class PersonDetailsForm(forms.Form):

    # Personal Details Field
    name = forms.CharField(label="Name", max_length=30)
    email = forms.EmailField(label="E-mail")
    contact = forms.CharField(max_length=10, label="Contact")
    address = forms.CharField(label="Address")

    # Skills Field
    skills_1 = forms.CharField(label="Skill 1")
    skills_2 = forms.CharField(label="Skill 2")
    skills_3 = forms.CharField(required=False, label="Skill 3")
    skills_4 = forms.CharField(required=False, label="Skill 4")

    # Soft Skills 
    soft_skills_1 = forms.CharField(label="Soft Skill 1")
    soft_skills_2 = forms.CharField(label="Soft Skill 2")
    soft_skills_3 = forms.CharField(required=False, label="Soft Skill 3")
    soft_skills_4 = forms.CharField(required=False, label="Soft Skill 4")

    # Experience Field
    experience_1_title = forms.CharField(label="Job Title")
    experience_1_dur = forms.CharField(label="Job Duration")
    experience_1_cname = forms.CharField(label="Company Name")
    experience_1_desc = forms.CharField(label="Job Description", widget=forms.Textarea)
    experience_2_title = forms.CharField(required=False)
    experience_2_dur = forms.CharField(required=False)
    experience_2_cname = forms.CharField(required=False, label="Company Name")
    experience_2_desc = forms.CharField(required=False,label="Job Description", widget=forms.Textarea)

    # Education Field
    education_1=forms.CharField(label="Degree obtained")
    education_1_dur=forms.CharField(label="Duration")
    education_1_name = forms.CharField(label="College Name")
    education1_score=forms.CharField(label="Score")
    education_2=forms.CharField(label="Degree obtained")
    education_2_dur=forms.CharField(label="Duration")
    education_2_name = forms.CharField(label="College Name")
    education2_score=forms.CharField(label="Score")

    # Project Fields
    project_1 = forms.CharField(label="Project Name")
    project_1_desc = forms.CharField(label="Project Description", required=False, widget=forms.Textarea)
    # project_1_url = forms.CharField(label="Project Url", required=False, widget=forms.URLField,)
    project_2 = forms.CharField(label="Project Name")
    project_2_desc = forms.CharField(label="Project Description", required=False, widget=forms.Textarea)
    # project_2_url = forms.CharField(label="Project Url", required=False, widget=forms.URLField)
    project_3 = forms.CharField(label="Project Name", required=False)
    project_3_desc = forms.CharField(label="Project Description", required=False, widget=forms.Textarea)
    # project_3_url = forms.CharField(label="Project Url", required=False, widget=forms.URLField)
