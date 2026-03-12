from django.contrib import admin

from .models import Ingredient, Profile, Recipe, RecipeImage, RecipeIngredient


# This handles Bonus Point 2: The Inline Admin
class RecipeIngredientInline(admin.TabularInline):
    model = RecipeIngredient
    extra = 1  # How many blank ingredient rows to show by default


class RecipeImageInline(admin.TabularInline):
    model = RecipeImage
    extra = 1


# This handles Bonus Point 1: The Recipe Admin panel
class RecipeAdmin(admin.ModelAdmin):
    model = Recipe
    inlines = [RecipeIngredientInline, RecipeImageInline]


# Registering the models so they appear in the admin site
admin.site.register(Ingredient)
admin.site.register(Profile)
admin.site.register(Recipe, RecipeAdmin)
