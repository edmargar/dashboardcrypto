from rest_framework import serializers
from .models import Exchange

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

class ExchangeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exchange
        exclude = []