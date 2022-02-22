from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets
from .serializers import ExchangeSerializer
from .models import Exchange


class ExchangeViewSet(viewsets.ModelViewSet):
    serializer_class = ExchangeSerializer
    queryset = Exchange.objects.all()
