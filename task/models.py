from django.db import models


# Create your models here.
class Task(models.Model):
    name = models.CharField(max_length=50, blank=True)
    description = models.TextField()
    deadline = models.DateTimeField()
    status = models.CharField(max_length=32)

    added = models.DateTimeField(auto_now_add=True)
