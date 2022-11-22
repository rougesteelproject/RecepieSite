from collections import Counter
from django.shortcuts import render
from django.http import HttpResponse
from . import models
from django.db.models import F, Max

#You can't import to keep, but you can copy paste.
# TODO stretch goal a javascript copy to clipboard button

#TODO stretch goal replace Counter with the solution here: https://github.com/python/typeshed/issues/3438 and have 1.5 cups instead of 3x half-cups

#TODO stretch goal have recepies be links to full instructions

#TODO stretch goal fill in recipes with new ones from another site
#   "New List" adds this recipe to the database

def requeue(recipes):
    for recipe in recipes:
    #We'll only have the 14 to work with
    #do it as a batch, so they move in segments

    #the preference_priority determines how often something should repeat, higher preference means the queue value is lower
    #The more you like something, the more often it will repeat

    #Five scales:
        #biweekly = 5
        max_queue = recipes.aggregate(Max('queue_value')).get('queue_value__max')

        if max_queue == 0:
            max_queue = 2

        if recipe.preference_priority == 5:
            recipe.queue_value = 0
            #set to 0
        if recipe.preference_priority == 4:
        #love, quarter of the list = 4:
            recipe.queue_value= max_queue/4 + 1
        #normal, half of the list = 3
        if recipe.preference_priority == 3:
            recipe.queue_value= max_queue/2 + 1
            #TODO must I put a round() in here?
        if recipe.preference_priority == 2:
        #okay = 2, 3/4 of the list:
            recipe.queue_value= max_queue* (3/4) + 1
        #less: end of the list = 1
        if recipe.preference_priority == 1:
            recipe.queue_value= max_queue+ 1
        #hate/never = 0
        if recipe.preference_priority == 0: 
            recipe.queue_value  -=1
            #TODO set to -1?
        recipe.save()

# Create your views here.
def home(request):

    ingredient_counter = Counter()

    recipes = models.Recipe.objects.filter(queue_value = 0)[:14]
    #TODO put in up to 14 recipes
    #[:14] get only 14 recipes
    #TODO check if this will bug when more than 14 have a q_v of 0
    #TODO if you can't get 14 recipes len(recipes) < 14, recipes= recipes + models.Recipe.objects.all()[:(14 - len(recipes))]
    #order by the queue value ascending

    #TODO a sllider form for each recepie to determine what pref_priority a recepie has
        #Default to the recipe's current pref_priority
    #TODO update preference button

    for recipe in recipes:
        ingredient_counter.update(recipe.ingredients)
        print(recipe.queue_value)

    if request.method == 'POST':
        #a save (accept recipe list) button that updates queue_value

        #on new_list, update the queue_value to put back into the queue
        requeue(recipes= recipes)
        
        #then reduce each recipe's queue_value by 1
        print('update')
        models.Recipe.objects.update(queue_value = F('queue_value') - 1)

        context = {
        'recipes': recipes,
        'ingredient_list': ingredient_counter.items()
        }
        return render(request, 'recipes/meal_plan.html', context)
    else:

        context = {
        'recipes': recipes,
        'ingredient_list': ingredient_counter.items()
        }
        return render(request, 'recipes/meal_plan.html', context)