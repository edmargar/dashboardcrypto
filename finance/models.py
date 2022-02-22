from django.db import models
#from crypto.models import Crypto
from exchange.models import Exchange
import datetime

class Negotiation(models.Model):
    TIPO_CHOICES = (
        ("C", "Compra"),
        ("V", "Venda"),
        ("S", "Stake")
    )

    tipo = models.CharField(max_length=1, choices=TIPO_CHOICES, blank=False)
    valor_operacao = models.FloatField()
    roi = models.FloatField(blank=True)
    quantidade = models.FloatField()
    cryptomoeda = models.ManyToManyField("crypto.Crypto")
    exchange = models.ManyToManyField("exchange.Exchange")
    data = models.DateField(default=datetime.date.today)


    def __str__(self):
        moeda = self.cryptomoeda.get()
        return self.tipo +" | "+ str(moeda) +" | "+ str(self.data)
