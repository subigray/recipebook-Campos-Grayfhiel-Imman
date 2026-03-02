from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Recipe

def recipe_list(request):
    recipes = Recipe.objects.all() 
    ctx = { "recipes": recipes }
    return render(request, 'recipe_list.html', ctx)

# This decorator forces the user to log in before seeing the detail page 
@login_required 
def recipe_detail(request, pk):
    recipe = Recipe.objects.get(id=pk) 
    ctx = { "recipe": recipe }
    return render(request, 'recipe_detail.html', ctx)