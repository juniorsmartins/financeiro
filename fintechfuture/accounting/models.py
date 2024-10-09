from random import choice, choices

from django.db import models
from enum import Enum
from django.db.models.utils import make_model_tuple

class TypeOperation(Enum):
    DEBITO = 1
    CREDITO = 2

class CostCenter(Enum):
    ALIMENTACAO = 1
    ALUGUEL = 2
    EDUCACAO = 3
    ELETRONICOS = 4
    ESPORTE = 5
    DECORACAO = 6
    INVESTIMENTO = 7
    LAZER = 8
    PET = 9
    PENSAO = 10
    SALARIO = 11
    SAUDE = 12
    SERVICOS = 13
    SUPLEMENTACAO = 14
    TELEFONIA = 15
    TRANSPORTE = 16
    VESTUARIO = 17
    OUTROS = 18

# Create your models here.
class Base(models.Model):
    creationDate = models.DateTimeField(auto_now_add=True)
    updateDate = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)

    class Meta:
        abstract = True

class Launch(Base):
    description = models.CharField(max_length=250) # Descrição
    typeOperation = models.CharField(max_length=10, choices=TypeOperation) # Tipo de Operação - Débito ou Crédito
    amount = models.FloatField() # Valor da transação
    launchDate = models.DateField() # Data de Lançamento
    costCenter = models.CharField(max_length=50, choices=TypeOperation) # Centro de Custo - categoria
    supplier = models.CharField(max_length=50) # Fornecedor origem/destino

