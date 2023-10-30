from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Images(models.Model):
    name = models.CharField(max_length=30)
    image = models.ImageField(upload_to='images/', blank=True, null=True)

    def insertDeatils(self, name, image):
        self.name = name
        self.image = image

        self.save()