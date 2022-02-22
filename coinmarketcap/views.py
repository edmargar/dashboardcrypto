from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import action
from requests import Request, Session
import json
import os
from dotenv import load_dotenv
from rest_framework import viewsets
from django.apps import apps

from .serializers import CMCSerializer
from .models import Coinmarketcap


class CMCViewSet(viewsets.ModelViewSet):
    serializer_class = CMCSerializer
    queryset = Coinmarketcap.objects.all()

    load_dotenv()
    endpoint = {
        'quotes': '/v1/cryptocurrency/quotes/latest',
        'info': '/v1/cryptocurrency/info',
        'list': '/v1/cryptocurrency/listings/latest'
    }
    key = os.getenv('COINMARKETCAP_API_KEY')
    url = f'https://pro-api.coinmarketcap.com'

    def getAPI(self, uri, parameters):
        headers = {
            'Accepts': 'application/json',
            'X-CMC_PRO_API_KEY': self.key,
        }
        session = Session()
        session.headers.update(headers)


        url = self.url+uri
        response = session.get(url, params=parameters)
        data = json.loads(response.text)

        return data

    def getValue(self, slug, country):
        """
            todo:Hoje a função faz um get por cripto, existe a possibilidade de passar varios slug e a api retorna as informações de todas, então devo alterar isso
            no futuro para que o sistema faça uma requisição apenas e trate tudo como lista.
        """
        uri = self.endpoint.get("quotes")

        if country == 'BR':
            currency = 'BRL'
        else:
            currency = 'USD'

        params = {
            'slug': str.lower(slug),
            'convert': currency
        }

        response = self.getAPI(self, uri, params)
        data = response["data"]

        id = next(iter(data.items()))
        id = str(id[0])

        data = data[id]["quote"][currency]["price"]

        return data

    def createCrypto(self, crypto):
        Crypto = apps.get_model('crypto.Crypto')
        try:
            C = Crypto()
            C.nome = crypto.name
            C.sigla = crypto.symbol
            C.rede = "Auto"
            C.wallet = ""
            C.exchange = ""
            C.coinmarketcap = crypto.id

            Crypto.save()

        except Exception as e:
            raise e

    @action(methods=['GET'], detail=True)
    def createCmc(self, request, pk):
        query_params = self.request.query_params
        slug = query_params.get('slug', None)
        if not slug:
            return Response('Parametro não reconhecido!')

        uri = self.endpoint.get("quotes")
        slug = str.lower(slug)
        params = {
            'slug': slug
        }

        response = self.getAPI(uri, params)
        data = response["data"]

        id = next(iter(data.items()))
        id = id[0]

        data = data[str(id)]

        try:
            coinmarketcap = Coinmarketcap()
            coinmarketcap.id_cmc = data["id"]
            coinmarketcap.name = data["name"]
            coinmarketcap.symbol = data["symbol"]
            coinmarketcap.slug = data["slug"]
            coinmarketcap.max_supply = data["max_supply"]
            coinmarketcap.circulating_supply = data["circulating_supply"]

            self.createCrypto(coinmarketcap)
            coinmarketcap.save()

            result = 'Dados gravados com sucesso!'
            return Response(result)
        except Exception as e:
            raise e
