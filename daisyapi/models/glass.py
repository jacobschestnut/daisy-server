from django.db import models

class Glass(models.Model):
    
    label = models.CharField(max_length=55)