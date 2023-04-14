from django.db import models

# Create your models here.
class ToDo(models.Model):
    todo = models.CharField(max_length=100)