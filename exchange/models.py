from django.db import models


class Exchange(models.Model):
    TIPO_CHOICES = (
        ("C", "Compra/Venda"),
        ("S", "Stake")
    )

    nome = models.CharField(max_length=50)
    Link = models.URLField(max_length=200)
    usuario = models.CharField(max_length=50)
    senha = models.CharField(max_length=50)
    anotacoes = models.TextField(max_length=500, blank=True)
    tipo = models.CharField(max_length=1, choices=TIPO_CHOICES, blank=False)


    def __str__(self):
        return self.nome