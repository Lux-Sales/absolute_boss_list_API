from rest_framework import validators, viewsets
from rest_framework import permissions
from .serializes import PlayerSerializer
from .models import Player

class PlayerViewSet(viewsets.ModelViewSet):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer
    permission_classes = [permissions.AllowAny]