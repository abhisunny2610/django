# Generated by Django 4.2.4 on 2023-12-02 21:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PersonDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('profession', models.CharField(max_length=50)),
                ('profile', models.TextField()),
                ('contact', models.CharField(max_length=10)),
                ('email', models.EmailField(max_length=254)),
                ('city', models.CharField(max_length=30)),
                ('github', models.URLField(blank=True, null=True)),
                ('linkedin', models.URLField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='SkillsDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skill_1', models.CharField(max_length=20)),
                ('skill_2', models.CharField(max_length=20)),
                ('skill_3', models.CharField(max_length=20)),
                ('skill_4', models.CharField(blank=True, max_length=30, null=True)),
                ('skill_5', models.CharField(blank=True, max_length=30, null=True)),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.persondetails')),
            ],
        ),
        migrations.CreateModel(
            name='ProjectDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_1', models.CharField(max_length=50)),
                ('project_1_url', models.URLField(blank=True, null=True)),
                ('project_1_desc', models.TextField(blank=True, null=True)),
                ('project_2', models.CharField(max_length=50)),
                ('project_2_url', models.URLField(blank=True, null=True)),
                ('project_2_desc', models.TextField(blank=True, null=True)),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.persondetails')),
            ],
        ),
        migrations.CreateModel(
            name='ExperienceDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('experience_1', models.CharField(max_length=30)),
                ('experience_1_company', models.CharField(max_length=50)),
                ('experience_1_start', models.DateField()),
                ('experience_1_end', models.DateField()),
                ('experience_1_description', models.TextField(blank=True, null=True)),
                ('experience_2', models.CharField(blank=True, max_length=30, null=True)),
                ('experience_2_company', models.CharField(blank=True, max_length=50, null=True)),
                ('experience_2_start', models.DateField()),
                ('experience_2_end', models.DateField()),
                ('experience_2_description', models.TextField(blank=True, null=True)),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.persondetails')),
            ],
        ),
        migrations.CreateModel(
            name='EducationDeatils',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('education_1', models.CharField(max_length=30)),
                ('education_1_college', models.CharField(max_length=50)),
                ('education_1_start', models.DateField()),
                ('education_1_end', models.DateField()),
                ('education_1_description', models.TextField(blank=True, null=True)),
                ('education_2', models.CharField(blank=True, max_length=30, null=True)),
                ('education_2_college', models.CharField(blank=True, max_length=50, null=True)),
                ('education_2_start', models.DateField()),
                ('education_2_end', models.DateField()),
                ('education_2_description', models.TextField(blank=True, null=True)),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.persondetails')),
            ],
        ),
    ]
