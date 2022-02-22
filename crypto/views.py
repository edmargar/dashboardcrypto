from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets
from .serializers import CryptoSerializer
from .models import Crypto


class CryptosViewSet(viewsets.ModelViewSet):
    """
        Antes de cadastrar uma moeda, verifique se ela existe em api/coinmarketcap, caso não exista
        acesse o link api/coinmarketcap/cmc/createCmc/?slug= nome da cripto que será cadastrada, com isso o
        sistema ira buscar e cadastrar os dados dela para que o vinculo entre as duas tabelas seja criado.
    """
    serializer_class = CryptoSerializer
    queryset = Crypto.objects.all()
