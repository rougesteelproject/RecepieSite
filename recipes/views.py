from collections import Counter
from django.shortcuts import render
from django.http import HttpResponse
from . import models

#You can't import to keep, but you can copy paste.
# TODO a javascript copy to clipboard button

#TODO replace Counter with the solution here: https://github.com/python/typeshed/issues/3438 and have 1.5 cups instead of 3x half-cups

#TODO have recepies be links to full instructions

# Create your views here.
def home(request):
    ingredient_counter = Counter()

    recipes = models.Recipe.objects.all()[:14]
    #[:14] get only 14 recipes
    # TODO where they're not stale (filter())
    #TODO stale-ness affected by repetition_multiplier

    #TODO the preference_repetition_multiplier determines how often something should repeat
    #   The more you like something, the more often it will repeat
    #   Five scales from love = once every two weeks/ once in every generation, 'Very often = 2x as often', normal = 1x,  'less often = 0.5x', hate = never

    for recipe in recipes:
        ingredient_counter.update(recipe.ingredients)

    if request.method == 'POST':
        #a save (accept recipe list) button that updates last_used
        for recipe in recipes:
            recipe.save()
    else:

        context = {
        'recipes': recipes,
        'ingredient_list': ingredient_counter.items()
        }
        return render(request, 'recipes/meal_plan.html', context)