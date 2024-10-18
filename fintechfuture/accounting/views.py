from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import CashBookCPF, DebitRegister, CreditRegister
from .serializers import CashBookCPFSerializer, DebitRegisterSerializer, CreditRegisterSerializer


class CashBookCPFAPIView(APIView):
    """
    API de livro de caixa
    """
    def get(self, request):
        cashBookCPF = CashBookCPF.objects.all()
        serializer = CashBookCPFSerializer(cashBookCPF, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CashBookCPFSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class DebitRegisterAPIView(APIView):
    """
    API de Registros de Débito
    """
    def get(self, request):
        debitRegisters = DebitRegister.objects.all()
        serializer = DebitRegisterSerializer(debitRegisters, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = DebitRegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class CreditRegisterAPIView(APIView):
    """
    API de Registros de Crédito
    """
    def get(self, request):
        creditRegisters = CreditRegister.objects.all()
        serializer = CreditRegisterSerializer(creditRegisters, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CreditRegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


