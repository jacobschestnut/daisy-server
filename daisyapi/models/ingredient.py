from django.db import models
from daisyapi.models import IngredientType

class Ingredient(models.Model):
    
    name = models.CharField(max_length=55)
    type = models.ForeignKey(IngredientType, related_name="ingredient_type")