from django.db import models
from boss_list.models import BossList


class Player(models.Model):
    name = models.CharField(max_length=255, unique=True)
    vocation = models.CharField(max_length=255)
    team = models.CharField(max_length=255)
    boss_list = models.ForeignKey(BossList, on_delete=models.CASCADE, null=False, related_name='players')



