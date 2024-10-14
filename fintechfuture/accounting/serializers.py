from rest_framework import serializers
from .models import CashBookCPF, DebitRegister, CreditRegister

class CashBookCPFSerializer(serializers.ModelSerializer):

    class Meta:
        model = CashBookCPF
        fields = (
            'cpf',
            'yearReference',
            'created',
            'updated',
            'active'
        )

class DebitRegisterSerializer(serializers.ModelSerializer):

    class Meta:
        model = DebitRegister
        fields = (
            'description',
            'typeOperation',
            'amount',
            'launchDate',
            'costCenter',
            'supplier',
            'cashBook',
            'created',
            'updated',
            'active'
        )

class CreditRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = CreditRegister
        fields = (
            'description',
            'typeOperation',
            'amount',
            'launchDate',
            'costCenter',
            'supplier',
            'cashBook',
            'created',
            'updated',
            'active'
        )


