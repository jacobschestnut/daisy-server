from django.db import models

class Preparation(models.Model):
    
    label = models.CharField(max_length=55)