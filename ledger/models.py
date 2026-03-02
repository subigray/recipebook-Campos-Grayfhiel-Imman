from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User # Required for the Profile model

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE) # [cite: 45]
    name = models.CharField(max_length=50) # [cite: 46]
    short_bio = models.TextField() # TextField naturally accommodates >255 chars [cite: 47]

    def __str__(self):
        return self.name

class Ingredient(models.Model):
    # (Keep your existing Ingredient code here)
    ...

class Recipe(models.Model):
    name = models.CharField(max_length=100)
    
    # New fields for Lab 3:
    # We use null=True temporarily so existing recipes don't crash the database
    author = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="recipes", null=True) # [cite: 49-50]
    created_on = models.DateTimeField(auto_now_add=True, null=True) # [cite: 51]
    updated_on = models.DateTimeField(auto_now=True, null=True) # [cite: 52]

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('recipe_detail', args=[str(self.id)])

class RecipeIngredient(models.Model):
    # (Keep your existing RecipeIngredient code here)
    ...