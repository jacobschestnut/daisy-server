from django.db import models

class Ice(models.Model):
    
    label = models.CharField(max_length=55)
    img_url = models.CharField(max_length=1000)