from django.contrib import admin
from . import models


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'create_time'
    )


class OrderAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'customer',
        'order_date'
    )


class OrderItemAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'order',
        'product'
    )


class InvoiceAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'order'
    )


class TransactionAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'invoice',
        'transaction_date',
        'amount',
        'status'
    )


admin.site.register(models.Product, ProductAdmin)
admin.site.register(models.Order, OrderAdmin)
admin.site.register(models.OrderItem, OrderItemAdmin)
admin.site.register(models.Invoice, InvoiceAdmin)
admin.site.register(models.Transaction, TransactionAdmin)
