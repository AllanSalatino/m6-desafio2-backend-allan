from django.db import models

class OpcoesTransacoes(models.TextChoices):
    DEB = "Débito"
    BOL = "Boleto"
    FIN = "Financiamento"
    CRE = "Crédito"
    REC = "Recebimento"
    VEN = "Vendas"
    TED = "Recebimnto TED"
    DOC = "Recebimento DOC"
    ALU = "Aluguel"


class Transacao(models.Model):
    
    tipo = models.CharField(
        max_length=15,
        choices=OpcoesTransacoes.choices
    )
    data = models.DateField(max_length=8)
    valor = models.IntegerField()
    cpf = models.CharField(max_length=11)
    cartao = models.CharField(max_length=12)
    hora = models.CharField(max_length=8)
    dono_da_loja = models.CharField(max_length=14)
    nome_loja = models.CharField(max_length=19)
