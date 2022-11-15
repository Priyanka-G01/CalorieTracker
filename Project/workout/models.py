from unittest.util import _MAX_LENGTH
from django.db import models
from django.contrib.auth.models import User
from bmi.models import Bmi
# Create your models here.

class Workout(models.Model):
    name = models.CharField(max_length = 100)
    met = models.FloatField()

    def __str__(self):
        return self.name

class CaloriesLostInDay(models.Model):
    name = models.ForeignKey(Workout, on_delete = models.CASCADE)
    weight = models.FloatField()
    duration = models.FloatField()
    total = models.FloatField()
    date = models.DateField(auto_now_add = True)
    