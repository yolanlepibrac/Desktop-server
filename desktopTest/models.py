from django.db import models


class Note(models.Model):
    value = models.CharField(max_length=80000)
    title = models.CharField(max_length=100)
