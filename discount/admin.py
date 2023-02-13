from django.contrib import admin

from .models import *


@admin.register(Card)
class CardAdmin(admin.ModelAdmin):
    list_filter = ['status', 'seria', 'id']
    date_hierarchy = 'date_created'
    search_fields = ['id']


@admin.register(CardStatus)
class CardStatusAdmin(admin.ModelAdmin):
    list_filter = ['name', 'id']
    search_fields = ['name']


@admin.register(CardSeries)
class CardSeriesAdmin(admin.ModelAdmin):
    list_filter = ['name', 'id']
    search_fields = ['name']


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_filter = ['name', 'price', 'discount']
    search_fields = ['name']


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_filter = ['date_created', 'card', 'id']
    date_hierarchy = 'date_created'
    search_fields = ['card']


@admin.register(OrderProduct)
class OrderProductAdmin(admin.ModelAdmin):
    list_filter = ['product', 'order', 'id']
    search_fields = ['product', 'order']
