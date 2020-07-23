from django.db import models

# Create your models here.
class AllBuilds(models.Model):
    title = models.CharField(max_length=300)
    image = models.ImageField(upload_to='all_builds_images/')