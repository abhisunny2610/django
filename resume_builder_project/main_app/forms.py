from django import forms

# validators=[RegexValidator(regex='^(\+?\d{1,3})?[-.\s]?\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}$')]


class PersonDetails(forms.Form):

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

    # Experience Field
    experience_1_title = forms.CharField()
    experience_1_dur = forms.CharField()
    experience_1_desc = forms.CharField()
    experience_2_title = forms.CharField(required=False)
    experience_2_dur = forms.CharField(required=False)
    experience_2_desc = forms.CharField(required=False)

    # Education Field
    education_1=forms.CharField(label="Degree obtained")
    education_1_dur=forms.CharField(label="Duration")
    education_1_name = forms.CharField(label="College Name")
    education1_score=forms.CharField()
    education_2=forms.CharField()
    education_2_dur=forms.CharField()
    education2_score=forms.CharField()