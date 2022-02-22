from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets
from .serializers import Walleterializer
from .models import Wallet


class WalletViewSet(viewsets.ModelViewSet):
    serializer_class = Walleterializer
    queryset = Wallet.objects.all()
