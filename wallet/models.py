from django.db import models


class Wallet(models.Model):
    nome = models.CharField(max_length=50)
    palavra_passe = models.CharField(max_length=150)
    usuario = models.CharField(max_length=50)
    senha = models.CharField(max_length=50)
    link = models.URLField(max_length=200)
    anotacoes = models.TextField(max_length=500, blank=True)


    def __str__(self):
        return self.nome
