# Generated by Django 4.2.4 on 2023-11-08 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_by', models.CharField(default='', max_length=40, null=True)),
                ('description', models.TextField(max_length=5000, null=True)),
                ('title', models.CharField(default='', max_length=200, null=True)),
            ],
        ),
    ]
