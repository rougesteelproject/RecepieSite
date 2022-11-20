from collections import Counter
from django.shortcuts import render
from django.http import HttpResponse
from . import models

#TODO the preference_repetition_multiplier determines how often something should repeat
#   The more you like something, the more often it will repeat
#   Five scales from love = once every two weeks/ once in every generation, 'Very often = 2x as often', normal = 1x,  'less often = 0.5x', hate = never

#You can't import to keep, but you can copy paste.
# TODO a copy to clipboard button

#TODO replace Counter with the solution here: https://github.com/python/typeshed/issues/3438 and have 1.5 cups instead of 3x half-cups

#TODO have recepies be links to full instructions

# Create your views here.
def home(request):
    ingredient_counter = Counter()

    recipes = models.Recipe.objects.all()
    #TODO get only 14 recipes, where they're not stale
    #TODO stale-ness affected by repetition_multiplier

    #TODO an accept recipe button that updates last_used
    #TODO DB stretch goal, the last time a recipe was accepted/saved to the 14-day calendar

    for recipe in recipes:
        ingredient_counter.update(recipe.ingredients)

    context = {
    'recipes': recipes,
    'ingredient_list': ingredient_counter.items()
    }
    return render(request, 'recipes/meal_plan.html', context)