from django.db import models

# Create your models here.
class Images(models.Model):
    name = models.CharField(max_length=30, null=True, default="")
    image = models.ImageField(upload_to='images/', blank=True, null=True)

    def insertdata(self, name, image):
        self.name = name
        self.image = image

        self.save()