from rest_framework import serializers
from players.models import Player
from .models import BossList
from players.serializers import PlayersSerializer

class AddPlayerSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=255, required=True)
    vocation = serializers.CharField(max_length=255, required=True)
    team = serializers.CharField(max_length=255, required=True)
    
    def create(self, validated_data):
        boss_list = BossList.objects.last()
        player = Player.objects.create(**validated_data, boss_list=boss_list)
        return player

class BossListSerializer(serializers.ModelSerializer):
    players = PlayersSerializer(many=True, read_only=True)
    
    class Meta:
        model = BossList
        fields = ['title','players','secret_key']
        extra_kwargs = {'secret_key':{'write_only':True}}

    def create(self, validated_data):
        secret_key = validated_data.get('secret_key')
        boss_list = BossList.objects.last()

        if boss_list.secret_key != secret_key:
            raise serializers.ValidationError({'secret_key':'invalid secret key'}) 

        boss_list = BossList.objects.last()
        boss_list.title = validated_data['title']
        boss_list.save()
        return boss_list

    def update(self, validated_data):
        secret_key = validated_data.get('secret_key')
        boss_list = BossList.objects.last()

        if boss_list.secret_key != secret_key:
            raise serializers.ValidationError({'secret_key':'invalid secret key'})

        boss_list = BossList.objects.last()
        boss_list.secret_key = validated_data['new_secret_key']
        boss_list.save()



