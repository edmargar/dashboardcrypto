from rest_framework import serializers, permissions, mixins, generics
from .models import Coinmarketcap


class CMCSerializer(serializers.ModelSerializer):
    permission_classes = [permissions.AllowAny]

    class Meta:
        model = Coinmarketcap
        exclude = []


class CoinmarketcapSerializer(serializers.ModelSerializer):
    permission_classes = [permissions.AllowAny]
