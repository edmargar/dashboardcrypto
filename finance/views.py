from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets
from .serializers import NegotiationSerializer
from .models import Negotiation


class NegotiationViewSet(viewsets.ModelViewSet):
    serializer_class = NegotiationSerializer
    queryset = Negotiation.objects.all()
