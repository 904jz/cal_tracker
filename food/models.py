from django.db import models
from django.contrib.auth.models import User
from datetime import datetime as dt
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    carbs = models.FloatField()

    fat = models.FloatField()

    protein = models.FloatField()

    calories = models.FloatField()

    day_count = models.IntegerField()

    last_updated = models.DateField()

    