from django.db import models
from wallet.models import Wallet
from exchange.models import Exchange
from finance.models import Negotiation
from coinmarketcap.models import Coinmarketcap
from coinmarketcap.views import CMCViewSet


class Categoria(models.Model):
    nome = models.CharField(max_length=50, blank=True)
    sigla = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return '(' + self.sigla + ')' + self.nome

    class Meta:
        ordering = ['sigla']

class Crypto(models.Model):
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, blank=True, null=True)
    nome = models.CharField(max_length=50)
    sigla = models.CharField(max_length=10)
    objetivo = models.FloatField(null=True)
    rede = models.CharField(max_length=100)
    wallet = models.ManyToManyField("wallet.Wallet", blank=True)
    exchange = models.ManyToManyField("exchange.Exchange")
    coinmarketcap = models.OneToOneField("coinmarketcap.Coinmarketcap", on_delete=models.CASCADE, blank=True)

    def __str__(self):
        return self.sigla +' - '+ self.nome

    class Meta:
        ordering = ['nome']


    def cost(self):
        # negotiations = Negotiation.objects.filter(cryptomoeda=self.id, tipo="C")
        # sum_negotiations = 0
        #
        # for negotiation in negotiations:
        #     sum_negotiations = negotiation.valor_operacao
        #     sum_amount = negotiation.quantidade
        #
        # if sum_negotiations > 0:
        #     sum_negotiations = sum_negotiations/sum_amount
        sum_negotiations = self.totalInvested()/self.amount()

        return sum_negotiations

    def stake(self):
        negotiations = Negotiation.objects.filter(cryptomoeda=self.id, tipo="S")
        sum_negotiations = 0

        for negotiation in negotiations:
            sum_negotiations = sum_negotiations + negotiation.quantidade


        return sum_negotiations

    def currentPrice(self):
        slug = self.nome

        response = CMCViewSet.getValue(CMCViewSet, slug, 'BR')

        return response

    def totalInvested(self):
        purchases = Negotiation.objects.filter(cryptomoeda=self.id, tipo="C")
        total = 0

        for purchase in purchases:
            total = total + purchase.valor_operacao

        return total

    def amount(self):
        negotiations = Negotiation.objects.filter(cryptomoeda=self.id, tipo="C")
        sum_negotiations = 0

        for negotiation in negotiations:
            sum_negotiations = sum_negotiations + negotiation.quantidade

        return sum_negotiations
