from django.db import models
from daisyapi.models.cocktail import Cocktail
from daisyapi.models.ingredient import Ingredient
from daisyapi.models.unit import Unit

class CocktailIngredient(models.Model):
    
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    cocktail = models.ForeignKey(Cocktail, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=3, decimal_places=2)
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE)