from django.contrib.auth.models import User
from django.db import models


class Game(models.Model):
    name = models.CharField(max_length=100)
    time = models.DurationField()
    coach = models.CharField(max_length=250)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    age = models.TextField(default=0)
    GENDER = [('MALE', 'Male'), ('FEMALE', 'Female'), ('OTHER', 'Other')]
    gender = models.CharField(max_length=10, choices=GENDER, default='MALE')
    game = models.ForeignKey(Game, on_delete=models.CASCADE)


class Bookings(models.Model):
    game = models.CharField(max_length=250)
    date = models.DateTimeField(auto_now=False)
    time = models.DurationField()
    price = models.FloatField(default=300)



