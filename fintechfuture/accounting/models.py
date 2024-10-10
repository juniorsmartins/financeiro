from random import choice, choices

from django.db import models
from enum import Enum
from django.db.models.utils import make_model_tuple

class TypeOperation(Enum):
    DEBIT = 1
    CREDIT = 2

class CostCenter(Enum):
    FOOD = 1
    RENT = 2
    EDUCATION = 3
    ELETRONIC = 4
    SPORT = 5
    HOUSE = 6
    INVESTIMENT = 7
    ENTERTAINMENT = 8
    PET = 9
    PENSION = 10
    WAGE = 11
    HEALTH = 12
    SERVICES = 13
    SUPPLEMENTATION = 14
    TELEPHONY = 15
    TRANSPORT = 16
    CLOTHING = 17
    OTHER = 18

# Create your models here.
class Base(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)

    class Meta:
        abstract = True


class CashBook(Base):
    document = models.CharField(max_length=14, unique=True)
    yearReference = models.DateField()

    class Meta:
        verbose_name = 'CashBook'
        unique_together = ['document', 'yearReference']

    def __str__(self):
        return f'CashBook -> Documento: {self.document}; Ano de Referência: {self.yearReference}.'


class DebitRegister(Base):
    description = models.CharField(max_length=250) # Descrição
    typeOperation = models.CharField(max_length=10, choices=TypeOperation, default=TypeOperation.DEBIT) # Tipo de Operação - Débito ou Crédito
    amount = models.FloatField() # Valor da transação
    launchDate = models.DateField() # Data de Lançamento
    costCenter = models.CharField(max_length=50, choices=CostCenter) # Centro de Custo - categoria
    supplier = models.CharField(max_length=50) # Fornecedor origem/destino
    cashBook = models.ForeignKey(CashBook, related_name='CashBook', on_delete=models.CASCADE)

    class Meta:
        verbose_name = "DebitRegister"

    def __str__(self):
        return self.description


class CreditRegister(Base):
    description = models.CharField(max_length=250) # Descrição
    typeOperation = models.CharField(max_length=10, choices=TypeOperation, default=TypeOperation.CREDIT) # Tipo de Operação - Débito ou Crédito
    amount = models.FloatField() # Valor da transação
    launchDate = models.DateField() # Data de Lançamento
    costCenter = models.CharField(max_length=50, choices=CostCenter) # Centro de Custo - categoria
    supplier = models.CharField(max_length=50) # Fornecedor origem/destino
    cashBook = models.ForeignKey(CashBook, related_name='CashBook', on_delete=models.CASCADE)

    class Meta:
        verbose_name = "CreditRegister"

    def __str__(self):
        return self.description




