from django.db import models


class BossList(models.Model):
    title = models.CharField(max_length=255, unique=True)
    secret_key = models.CharField(max_length=255,null=True)