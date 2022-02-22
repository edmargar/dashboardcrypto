from rest_framework import serializers, permissions, mixins, generics
from .models import Crypto

"""class RedeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Network
        exclude = []

class WalletSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wallet
        exclude = []

class ExchangeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exchange
        exclude = []
"""

class CryptoSerializer(serializers.ModelSerializer):
    cost = serializers.ReadOnlyField()
    stake = serializers.ReadOnlyField()
    totalInvested = serializers.ReadOnlyField()
    amount = serializers.ReadOnlyField()
    currentPrice = serializers.ReadOnlyField()
    #permission_classes = [permissions.AllowAny]

    class Meta:
        model = Crypto
        exclude = []
