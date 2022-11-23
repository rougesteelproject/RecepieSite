# Overview

This app will give you two weeks of recipes, and an ingredient list that you can copy-paste into, say, Google Keep. To start the server, use the terminal to run `python manage.py runserver` from the RecepieSite folder. The website will run at localhost:8000 .

Use localhost:8000/admin to add your own recipes. Note that currently, due to a quirk of the ingredient summary mechanism, you'll have to put ingredients as whole-number amounts, meaning you'll have to write things like '"half cup rice": 3' to represent 1.5 cups.

I made this software so that I could generate grocery lists without doing it by hand.

[Software Demo Video](http://youtube.link.goes.here)

# Web Pages

The only web page is the home page, which shows you 14 recipes and the ingredients to make those recipes, including a master ingredient list at the bottom. The recipes are shown if they've made their wat to the bottom of the queue, which happens more frequently at higher 'priority_preference' values, up to once every two weeks at level 5.

# Development Environment

This was developed in Django using VSCode.

# Useful Websites

{Make a list of websites that you found helpful in this project}
* [Web Site Name](http://url.link.goes.here)
* [Web Site Name](http://url.link.goes.here)

# Future Work

* Clicking on a recipe should show you the recipe.
* A way to update preference priority from the home page.
* Users and conversion into a server model, rather than a personal application.
* Getting 14 recipes in cases where there are too few to create a full cycle.
* A 'copy to clipboard' button for the ingredient list
* Replace the counter with something that allows for fractional ingredients.
* Fill in the gaps with new recipes from another site.
