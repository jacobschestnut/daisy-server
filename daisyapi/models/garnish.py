from django.db import models

class Garnish(models.Model):
    
    label = models.CharField(max_length=55)