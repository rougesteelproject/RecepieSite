from django.db import models

# Create your models here.

class Recipe(models.Model):
    title = models.CharField(max_length=100)
    cookbook = models.TextField()
    instructions = models.TextField()
    ingredients = models.JSONField()

    preference_repetition_multiplier = models.FloatField()
    last_used = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title