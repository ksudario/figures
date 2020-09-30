from django.db import models
from django import forms
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User
WEAPONS_KINDS = (("Blade", "BLADE"), ("Spear", "SPEAR"), ("Gauntlet", "GAUNTLET"),)

# Create your models here.
 

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    favorite_weapon = models.CharField(max_length=50)


class Weapon(models.Model):
    name = models.CharField(max_length=50)
    kind = models.CharField(max_length=100, choices=WEAPONS_KINDS, default=WEAPONS_KINDS[2][0])
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
    def activities_for_figure(self):
        return self.activity_set.filter(figure=self.id)
 

class Activity(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateField('activity date')
    figure = models.ForeignKey(Figure, on_delete=models.CASCADE)
    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-date']


