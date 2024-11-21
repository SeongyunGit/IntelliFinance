from rest_framework import serializers
from .models import (
    companyList, companyListOption,
    IntegrationProduct, IntegrationProductOption
)

# companyList에 대한 직렬화
class CompanyListSerializer(serializers.ModelSerializer):
    class Meta:
        model = companyList
        fields = '__all__'

# companyListOption에 대한 직렬화
class CompanyListOptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = companyListOption
        fields = '__all__'

# IntegrationProduct에 대한 직렬화
class IntegrationProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = IntegrationProduct
        fields = '__all__'

# IntegrationProductOption에 대한 직렬화
class IntegrationProductOptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = IntegrationProductOption
        fields = '__all__'
