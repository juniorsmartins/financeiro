from django.urls import path

from .views import CashBookCPFAPIView, DebitRegisterAPIView, CreditRegisterAPIView

urlpatterns = [
    path('cash-book-cpf', CashBookCPFAPIView.as_view(), name='cash-book-cpf'),
    path('debit-register', DebitRegisterAPIView.as_view(), name='debit-register'),
    path('credit-register', CreditRegisterAPIView.as_view(), name='credit-register'),
]

