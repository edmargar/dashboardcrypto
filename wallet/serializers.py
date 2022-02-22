from rest_framework import serializers
from .models import Wallet

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


class Walleterializer(serializers.ModelSerializer):
    class Meta:
        model = Wallet
        exclude = []
