from django.shortcuts import render

# 1. View for the list of recipes (localhost:8000/recipes/list)
def recipe_list(request):
    # This is the data from "Recipe List Context.txt"
    ctx = {
        "recipes": [
            {
                "name": "Recipe 1",
                "ingredients": [
                    {"name": "tomato", "quantity": "3pcs"},
                    {"name": "onion", "quantity": "1pc"},
                    {"name": "pork", "quantity": "1kg"},
                    {"name": "water", "quantity": "1L"},
                    {"name": "sinigang mix", "quantity": "1 packet"}
                ],
                "link": "/recipe/1"
            },
            {
                "name": "Recipe 2",
                "ingredients": [
                    {"name": "garlic", "quantity": "1 head"},
                    {"name": "onion", "quantity": "1pc"},
                    {"name": "vinegar", "quantity": "1/2cup"},
                    {"name": "water", "quantity": "1 cup"},
                    {"name": "salt", "quantity": "1 tablespoon"},
                    {"name": "whole black peppers", "quantity": "1 tablespoon"},
                    {"name": "pork", "quantity": "1 kilo"}
                ],
                "link": "/recipe/2"
            }
        ]
    }
    # This sends the data 'ctx' to the 'recipe_list.html' template
    return render(request, 'recipe_list.html', ctx)


# 2. View for Recipe 1 (localhost:8000/recipe/1)
def recipe_1(request):
    # This is the data from "Recipe 1.txt"
    ctx = {
        "name": "Recipe 1",
        "ingredients": [
            {"name": "tomato", "quantity": "3pcs"},
            {"name": "onion", "quantity": "1pc"},
            {"name": "pork", "quantity": "1kg"},
            {"name": "water", "quantity": "1L"},
            {"name": "sinigang mix", "quantity": "1 packet"}
        ],
        "link": "/recipe/1"
    }
    return render(request, 'recipe_1.html', ctx)


# 3. View for Recipe 2 (localhost:8000/recipe/2)
def recipe_2(request):
    # This is the data from "Recipe 2.txt"
    ctx = {
        "name": "Recipe 2",
        "ingredients": [
            {"name": "garlic", "quantity": "1 head"},
            {"name": "onion", "quantity": "1pc"},
            {"name": "vinegar", "quantity": "1/2cup"},
            {"name": "water", "quantity": "1 cup"},
            {"name": "salt", "quantity": "1 tablespoon"},
            {"name": "whole black peppers", "quantity": "1 tablespoon"},
            {"name": "pork", "quantity": "1 kilo"}
        ],
        "link": "/recipe/2"
    }
    return render(request, 'recipe_2.html', ctx)