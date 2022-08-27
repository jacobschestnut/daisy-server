from django.db import models
from daisyapi.models import Glass, Ice, Garnish, Preparation

class Cocktail(models.Model):
    
    name = models.CharField(max_length=55)
    description = models.CharField(max_length=255)
    instructions = models.CharField(max_length=255)
    preparation = models.ForeignKey(Preparation, related_name="preparation")
    glass = models.ForeignKey(Glass, related_name="glass")
    ice = models.ForeignKey(Ice, related_name="ice")
    img_url = models.CharField(max_length=1000)