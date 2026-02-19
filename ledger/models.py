from django.db import models
from django.urls import reverse

# 1. Ingredient Model
class Ingredient(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('ingredient_detail', args=[str(self.id)])

# 2. Recipe Model
class Recipe(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('recipe_detail', args=[str(self.id)])

# 3. RecipeIngredient Model (Associative Entity)
class RecipeIngredient(models.Model):
    quantity = models.CharField(max_length=50)
    
    # The lab instructions require specific related_names for these Foreign Keys
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE, related_name="recipe")
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name="ingredients")

    def __str__(self):
        return f"{self.quantity} of {self.ingredient.name} in {self.recipe.name}"