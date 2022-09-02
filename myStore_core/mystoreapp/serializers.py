from rest_framework import serializers
from mystoreapp.models import Product, Sale, ItemsSold, Category


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [
            'id',
            'name',
            'category',
            'description',
            'price',
            'amount',
            'image',
        ]


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class SaleSerializer(serializers.ModelSerializer):
    pass


class ItemsSoldSerializer(serializers.ModelSerializer):
    pass
