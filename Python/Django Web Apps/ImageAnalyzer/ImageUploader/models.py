from django.db import models

# Create your models here.
class ImageInfo(models.Model):
    ImageName = models.CharField(max_length=100)
    Url = models.CharField(max_length=100)
    def __str__(self):
        return self.Url