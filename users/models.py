from django.db import models


class User(models.Model):
    name = models.CharField(max_length=255, unique=True)
    vocation = models.CharField(max_length=255)
    team = models.CharField(max_length=255)



