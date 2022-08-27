from tkinter import CASCADE
from django.db import models
from daisyapi.models.glass import Glass
from daisyapi.models.ice import Ice
from daisyapi.models.mixologist import Mixologist
from daisyapi.models.preparation import Preparation

class Cocktail(models.Model):
    
    name = models.CharField(max_length=55)
    creator = models.ForeignKey(Mixologist, on_delete=models.CASCADE)
    description = models.CharField(max_length=255)
    instructions = models.CharField(max_length=255)
    preparation = models.ForeignKey(Preparation, on_delete=models.CASCADE)
    glass = models.ForeignKey(Glass, on_delete=models.CASCADE)
    ice = models.ForeignKey(Ice, on_delete=models.CASCADE)
    img_url = models.CharField(max_length=1000)