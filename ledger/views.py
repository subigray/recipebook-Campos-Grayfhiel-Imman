from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .models import Recipe, RecipeImage


def recipe_list(request):
    recipes = Recipe.objects.all()
    ctx = {"recipes": recipes}
    return render(request, 'recipe_list.html', ctx)


@login_required
def recipe_detail(request, pk):
    recipe = get_object_or_404(Recipe, id=pk)
    ctx = {"recipe": recipe}
    return render(request, 'recipe_detail.html', ctx)


class RecipeCreateView(LoginRequiredMixin, CreateView):
    model = Recipe
    fields = ['name', 'author']
    template_name = 'recipe_form.html'

    def get_success_url(self):
        # Redirects to the newly created recipe's detail page
        return reverse_lazy(
            'recipe_detail',
            kwargs={'pk': self.object.pk}
        )


class RecipeImageCreateView(LoginRequiredMixin, CreateView):
    model = RecipeImage
    fields = ['image', 'description']
    template_name = 'recipeimage_form.html'

    def form_valid(self, form):
        # Attach the image to the correct recipe using the URL pk
        recipe = get_object_or_404(Recipe, pk=self.kwargs['pk'])
        form.instance.recipe = recipe
        return super().form_valid(form)

    def get_success_url(self):
        # Redirect back to the recipe detail page upon saving [cite: 18]
        return reverse_lazy(
            'recipe_detail',
            kwargs={'pk': self.kwargs['pk']}
        )

    def get_context_data(self, **kwargs):
        # Modify context for the bonus point link [cite: 31]
        context = super().get_context_data(**kwargs)
        context['recipe_pk'] = self.kwargs['pk']
        return context
    