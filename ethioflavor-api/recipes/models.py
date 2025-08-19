from django.db import models
from django.conf import settings

class Category(models.Model):
    name = models.CharField(max_length=100)

class Ingredient(models.Model):
    name = models.CharField(max_length=100)

class Recipe(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    instructions = models.TextField()
    ingredients = models.ManyToManyField(Ingredient)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    prep_time = models.PositiveIntegerField()
    cook_time = models.PositiveIntegerField()
    servings = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)