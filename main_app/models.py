from django.db import models
from django import forms
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User


TIMES = (
    ("M", "Morning"),
    ("A", "Afternoon"),
    ("E", "Evening"),
)

# Create your models here.
 

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    favorite_weapon = models.CharField(max_length=50)


class Weapon(models.Model):
    name = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    def get_absolute_url(self):
            return reverse('weapons_index')

class Figure(models.Model):
    name = models.CharField(max_length=150)
    type = models.CharField(max_length=150)
    cost = models.CharField(max_length=150)
    weapons = models.ManyToManyField(Weapon)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('detail', kwargs={'figure_id': self.id})

    def clean_for_today(self):
        return self.cleaning_set.filter(date=date.today()).count() >= len(TIMES)
 

class Cleaning(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateField('cleaning date')
    meal = models.CharField(
    max_length=1,
    choices=TIMES,
    default=TIMES[0][0]
  )
    figure = models.ForeignKey(Figure, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.get_time_display()} on {self.date}"

    class Meta:
        ordering = ['-date']

class Photo(models.Model):
    url = models.CharField(max_length=200)
    figure = models.ForeignKey(Figure, on_delete=models.CASCADE)

    def __str__(self):
        return f"Photo for figure_id: {self.figure_id} @{self.url}"


