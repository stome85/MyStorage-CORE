import django_filters
from django.db.models import Q
from mystoreapp import models


class ProductFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains')
    description = django_filters.CharFilter(lookup_expr='icontains')
    category = django_filters.CharFilter(lookup_expr='icontains')

    def findByCategory(queryset, value):
        return queryset.filter(Q(category_id=value))

    class Meta:
        model = models.Product
        fields = ['name', 'description', 'price']


class CategoryFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = models.Category
        fields = ['name']


class SaleFilter(django_filters.FilterSet):
    pass
