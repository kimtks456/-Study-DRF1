from django.db import models

# Create your models here.

class Mealplan(models.Model):
    title = models.CharField(max_length=100)
    meal_date = models.CharField(max_length=20)
    kind_of_meal = models.CharField(max_length=20)
    menu = models.CharField(max_length=200)