from django.db import models


class Player(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField(default=1)
    club = models.CharField(max_length=50)
    position = models.CharField(max_length=2)
    salary = models.BigIntegerField()
