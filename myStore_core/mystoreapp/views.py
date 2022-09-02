from rest_framework import viewsets, generics
from mystoreapp import serializers, filters, models


class ProductViewSet(viewsets.ModelViewSet):
    queryset = models.Product.objects.all()
    serializer_class = serializers.ProductSerializer
    filter_class = filters.ProductFilter


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = models.Category.objects.all()
    serializer_class = serializers.CategorySerializer
    filter_class = filters.CategoryFilter


class ListProductByCategory(generics.ListAPIView):
    def get_queryset(self):
        return models.Product.objects.filter(category=self.kwargs['category'])
    serializer_class = serializers.ProductSerializer


class SaleViewSet(viewsets.ModelViewSet):
    queryset = models.Sale.objects.all()
    serializer_class = serializers.SaleSerializer


class ItemSoldViewSet(viewsets.ModelViewSet):
    queryset = models.ItemsSold.objects.all()
    serializer_class = serializers.ItemsSoldSerializer
