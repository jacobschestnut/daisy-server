from django.db import models
from daisyapi.models import Ingredient, Unit, Cocktail, cocktail

class CocktailIngredient(models.Model):
    
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE, related_name="ingredient")
    cocktail = models.ForeignKey(Cocktail, on_delete=models.CASCADE, related_name="cocktail")
    amount = models.DecimalField(max_digits=3, decimal_places=2)
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE, related_name="unit")