from rest_framework import serializers
from .models import Negotiation
from crypto.models import Crypto


class NegotiationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Negotiation
        exclude = []
        depth = 2
