from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Notes(models.Model):
    title = models.CharField(max_length=30, null=True)
    description = models.TextField(max_length=2000, null=True)
    date = models.DateField(auto_now_add= True)
    user = models.ForeignKey(User, default=1, on_delete=models.DO_NOTHING)