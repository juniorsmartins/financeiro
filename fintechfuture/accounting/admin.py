from django.contrib import admin

# Register your models here.
from .models import CashBook, DebitRegister, CreditRegister

@admin.register(CashBook)
class CashBookAdmin(admin.ModelAdmin):
    list_display = ('document', 'yearReference', 'created', 'updated', 'active')


@admin.register(DebitRegister)
class DebitRegisterAdmin(admin.ModelAdmin):
    list_display = ('description', 'typeOperation', 'amount', 'launchDate', 'costCenter',
                    'supplier', 'cashBook', 'created', 'updated', 'active')


@admin.register(CreditRegister)
class CreditRegisterAdmin(admin.ModelAdmin):
    list_display = ('description', 'typeOperation', 'amount', 'launchDate', 'costCenter',
                    'supplier', 'cashBook', 'created', 'updated', 'active')


