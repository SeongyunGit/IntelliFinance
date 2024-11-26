from rest_framework import serializers
from .models import CurrencyExchange


# 환율
class CurrencyExchangeSerializer(serializers.ModelSerializer):
    class Meta:
        model = CurrencyExchange
        fields = '__all__'