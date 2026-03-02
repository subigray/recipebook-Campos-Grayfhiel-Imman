from django.contrib import admin
from .models import Ingredient, Recipe, RecipeIngredient
from .models import Ingredient, Recipe, RecipeIngredient, Profile

# This handles Bonus Point 2: The Inline Admin 
class RecipeIngredientInline(admin.TabularInline):
    model = RecipeIngredient
    extra = 1  # How many blank ingredient rows to show by default

# This handles Bonus Point 1: The Recipe Admin panel 
class RecipeAdmin(admin.ModelAdmin):
    model = Recipe
    inlines = [RecipeIngredientInline] # This connects the inline to the recipe

# Registering the models so they appear in the admin site
admin.site.register(Ingredient)
admin.site.register(Recipe, RecipeAdmin)

admin.site.register(Profile)