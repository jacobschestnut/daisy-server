from django.db import models
from daisyapi.models.mixologist import Mixologist
from daisyapi.models.cocktail import Cocktail

class Favorite(models.Model):

    mixologist = models.ForeignKey(Mixologist, on_delete=models.CASCADE)
    cocktail = models.ForeignKey(Cocktail, on_delete=models.CASCADE)