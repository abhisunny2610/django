# Generated by Django 4.2.4 on 2023-10-30 19:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('practice', '0002_alter_user_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('image', models.ImageField(blank=True, null=True, upload_to='media/images/')),
            ],
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]