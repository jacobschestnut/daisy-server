from django.db import models

from daisyapi.models.ingredient_type import IngredientType

class Ingredient(models.Model):
    
    name = models.CharField(max_length=55)
    type = models.ForeignKey(IngredientType, on_delete=models.CASCADE, related_name="ingredient_type")