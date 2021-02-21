from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import BossList
from rest_framework.views import APIView
from .serializers import AddPlayerSerializer, BossListSerializer


class BossListViewSet(viewsets.ModelViewSet):
    queryset = BossList.objects.all()
    serializer_class = BossListSerializer
    permission_classes = [permissions.AllowAny]

    def destroy(self, request,pk=None):
        boss_list = BossList.objects.last()

        if boss_list.secret_key != pk:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        boss_list.players.all().delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def update(self, request, pk=None):
        boss_list = BossList.objects.last()

        if boss_list.secret_key != pk: #PK = URL
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        
        boss_list.secret_key = request.data['new_secret_key']
        boss_list.save()        
        return Response(status=status.HTTP_200_OK)


class AddPlayerViewSet(APIView):
    def post(self, request, format=None):
        serializer = AddPlayerSerializer(data = request.data)
        if not serializer.is_valid():
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)





