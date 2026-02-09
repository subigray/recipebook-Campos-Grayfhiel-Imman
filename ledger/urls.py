from django.urls import path
from . import views  # This imports your views.py file so we can link to it

urlpatterns = [
    # This is for /recipes/list [cite: 11]
    path('recipes/list', views.recipe_list, name='recipe_list'),

    # This is for /recipe/1 [cite: 12]
    path('recipe/1', views.recipe_1, name='recipe_1'),

    # This is for /recipe/2 [cite: 13]
    path('recipe/2', views.recipe_2, name='recipe_2'),
]