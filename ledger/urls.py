from django.urls import path

from . import views


urlpatterns = [
    # Path 1: The Recipe List
    path('recipes/list', views.recipe_list, name='recipe_list'),

    # Path 2: The dynamic Recipe Detail using a unique key parameter (pk)
    path('recipe/<int:pk>', views.recipe_detail, name='recipe_detail'),
]
