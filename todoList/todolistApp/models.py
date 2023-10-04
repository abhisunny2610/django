from django.db import models

# Create your models here.
class Todos(models.Model):
    content = models.CharField(max_length=50)
    isCompleted = models.BooleanField()
