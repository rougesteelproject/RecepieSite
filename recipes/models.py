from django.db import models
from django.utils import timezone

# Create your models here.

class Recipe(models.Model):
    title = models.CharField(max_length=100)
    cookbook = models.TextField()
    instructions = models.TextField()
    ingredients = models.JSONField()

    preference_priority = models.IntegerField(default = 3)
    queue_value = models.IntegerField(default = 0)

    def __str__(self):
        return self.title