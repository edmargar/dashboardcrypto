from django.db import models


class Coinmarketcap(models.Model):
    id_cmc = models.IntegerField()
    name = models.CharField(max_length=50)
    symbol = models.CharField(max_length=10, blank=True)
    slug = models.CharField(max_length=50, blank=True)
    url = models.URLField(max_length=100, blank=True)
    logo = models.URLField(max_length=200, blank=True)
    max_supply = models.IntegerField(default=0, blank=True, null=True)
    circulating_supply = models.IntegerField(default=0, blank=True, null=True)

    def __str__(self):
        return self.name +' - '+ self.symbol

    class Meta:
        ordering = ['name']
