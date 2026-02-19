from django.shortcuts import render
from .models import Recipe

# View for the Recipe List
def recipe_list(request):
    # Fetch all recipes from the database
    recipes = Recipe.objects.all() 
    
    ctx = {
        "recipes": recipes
    }
    return render(request, 'recipe_list.html', ctx)

# View for the Recipe Detail (using the unique key 'pk' from the URL)
def recipe_detail(request, pk):
    # Fetch the specific recipe matching the ID in the URL
    recipe = Recipe.objects.get(id=pk) 
    
    ctx = {
        "recipe": recipe
    }
    return render(request, 'recipe_detail.html', ctx)