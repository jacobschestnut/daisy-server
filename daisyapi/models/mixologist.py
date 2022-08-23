from django.db import models
from django.contrib.auth.models import User


class Mixologist(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    img_url = models.CharField(max_length=1000)