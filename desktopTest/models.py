from django.db import models

# Create your models here.

class Notes(models.Model):
    value = models.CharField(max_length=8000)
    title = models.CharField(max_length=100)
