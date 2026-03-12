from django.urls import path

from . import views


urlpatterns = [
    path('recipes/list', views.recipe_list, name='recipe_list'),
    path('recipe/<int:pk>', views.recipe_detail, name='recipe_detail'),
    # URL for creating new recipes [cite: 13]
    path('recipe/add', views.RecipeCreateView.as_view(), name='recipe_add'),
    # URL for uploading images [cite: 17]
    path(
        'recipe/<int:pk>/add_image',
        views.RecipeImageCreateView.as_view(),
        name='recipe_image_add'
    ),
]
