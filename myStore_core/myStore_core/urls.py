"""myStore_core URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from mystoreapp.views import ProductViewSet, SaleViewSet, ItemSoldViewSet, CategoryViewSet, ListProductByCategory, SearchCategory
from rest_framework import routers

router = routers.DefaultRouter()
router.register('products', ProductViewSet, basename='Product')
router.register('categories', CategoryViewSet, basename='Category')
router.register('sale', SaleViewSet, basename='Sale')
router.register('items-sold', ItemSoldViewSet, basename='Items-sold')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('products/category/<int:category>', ListProductByCategory.as_view()),
    path('categories/search/<name>', SearchCategory.as_view())
]
