from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Todos(models.Model):
    content = models.CharField(max_length=100)
    isCompleted = models.BooleanField(default=False)
    user = models.ForeignKey(User, default=1, on_delete=models.DO_NOTHING)