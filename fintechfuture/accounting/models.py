from random import choice, choices

from django.db import models
from enum import Enum
from django.db.models.utils import make_model_tuple

class TypeOperation(Enum):
    DEBIT = 'DEBIT'
    CREDIT = 'CREDIT'

    @classmethod
    def choices(cls):
        return [(member.value, member.name) for member in cls]


class CostCenter(Enum):
    FOOD = 'FOOD'
    RENT = 'RENT'
    EDUCATION = 'EDUCATION'
    ELETRONIC = 'ELETRONIC'
    SPORT = 'SPORT'
    HOUSE = 'HOUSE'
    INVESTIMENT = 'INVESTIMENT'
    ENTERTAINMENT = 'ENTERTAIMENT'
    PET = 'PET'
    PENSION = 'PENSION'
    WAGE = 'WAGE'
    HEALTH = 'HEALTH'
    SERVICES = 'SERVICES'
    SUPPLEMENTATION = 'SUPPLEMENTATION'
    TELEPHONY = 'TELEPHONY'
    TRANSPORT = 'TRANSPORT'
    CLOTHING = 'CLOTHING'
    OTHER = 'OTHER'

    @classmethod
    def choices(cls):
        return [(member.value, member.name) for member in cls]


# Create your models here.
class Base(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)

    class Meta:
        abstract = True


class CashBookCPF(Base):
    cpf = models.CharField(max_length=11)
    yearReference = models.DateField()

    class Meta:
        verbose_name = 'CashBookCPF'
        unique_together = ['cpf', 'yearReference']

    def __str__(self):
        return f'CashBookCPF -> CPF: {self.cpf}; Ano de Referência: {self.yearReference}.'


class DebitRegister(Base):
    description = models.CharField(max_length=250) # Descrição
    typeOperation = models.CharField(max_length=10, choices=TypeOperation.choices, default=TypeOperation.DEBIT) # Tipo de Operação - Débito ou Crédito
    amount = models.FloatField() # Valor da transação
    launchDate = models.DateField() # Data de Lançamento
    costCenter = models.CharField(max_length=50, choices=CostCenter.choices) # Centro de Custo - categoria
    supplier = models.CharField(max_length=50) # Fornecedor origem/destino
    cashBook = models.ForeignKey(CashBookCPF, related_name='debit_cashbookcpf', on_delete=models.CASCADE)

    class Meta:
        verbose_name = "DebitRegister"

    def __str__(self):
        return self.description


class CreditRegister(Base):
    description = models.CharField(max_length=250) # Descrição
    typeOperation = models.CharField(max_length=10, choices=TypeOperation.choices, default=TypeOperation.CREDIT) # Tipo de Operação - Débito ou Crédito
    amount = models.FloatField() # Valor da transação
    launchDate = models.DateField() # Data de Lançamento
    costCenter = models.CharField(max_length=50, choices=CostCenter.choices) # Centro de Custo - categoria
    supplier = models.CharField(max_length=50) # Fornecedor origem/destino
    cashBook = models.ForeignKey(CashBookCPF, related_name='credit_cashbookcpf', on_delete=models.CASCADE)

    class Meta:
        verbose_name = "CreditRegister"

    def __str__(self):
        return self.description




