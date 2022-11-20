from rest_framework import serializers
from django.contrib.auth.models import User
from .models import *


class StockSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stock
        exclude = ['id']

class PurchaseOrderSerializer(serializers.ModelSerializer):
    stock_id = serializers.CharField(max_length = 10)
    class Meta:
        model = PurchaseOrder
        fields = ['stock_id', 'stock_qty', 'price']

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = PurchaseOrder
        exclude = ['id', 'customer','stock']
