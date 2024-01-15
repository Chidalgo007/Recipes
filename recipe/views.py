from django.shortcuts import get_object_or_404, render
from .models import Recipe

def index(request):
    recipes = Recipe.objects.all()
    # Extracting ingredients list for each recipe
    context = {'recipes':recipes}
    return render(request, 'recipe/index.html', context)

def recipe(request, recipe_id):
    current_recipe = get_object_or_404(Recipe, id=recipe_id)

    # Find the previous and next recipes
    previous_recipe = Recipe.objects.filter(id__lt=current_recipe.id).order_by('-id').first()
    next_recipe = Recipe.objects.filter(id__gt=current_recipe.id).order_by('id').first()

    context = {
        'recipe': current_recipe,
        'ingredients_list': [current_recipe.get_ingredients_list()],
        'instruction_list': [current_recipe.get_instruction_list()],
        'previous_recipe': previous_recipe,
        'next_recipe': next_recipe,
    }

    return render(request, 'recipe/recipe.html', context)    