from django.contrib import admin

# Register your models here.
from .models import CashBookCPF, DebitRegister, CreditRegister

@admin.register(CashBookCPF)
class CashBookCPFAdmin(admin.ModelAdmin):
    list_display = ('cpf', 'yearReference', 'created', 'updated', 'active')


@admin.register(DebitRegister)
class DebitRegisterAdmin(admin.ModelAdmin):
    list_display = ('description', 'typeOperation', 'amount', 'launchDate', 'costCenter',
                    'supplier', 'cashBook', 'created', 'updated', 'active')


@admin.register(CreditRegister)
class CreditRegisterAdmin(admin.ModelAdmin):
    list_display = ('description', 'typeOperation', 'amount', 'launchDate', 'costCenter',
                    'supplier', 'cashBook', 'created', 'updated', 'active')


