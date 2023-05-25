from django.db import models


class Departments(models.Model):
    title = models.CharField(max_length=50)
    text = models.TextField()
