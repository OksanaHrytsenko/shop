from django.contrib.auth import get_user_model
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ModelViewSet

from api.serializers import (BrandSerializer, CategorySerializer,
                             CustomerSerializer, ProductSerializer)
from core.permissions import IsSuperUser
from product.models import Brand, Category, Product


class CustomerViewSet(ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = CustomerSerializer


class ProductDetailView(RetrieveAPIView):
    permission_classes = [AllowAny]
    serializer_class = ProductSerializer

    def get_queryset(self):
        return Product.objects.all()

    def get_object(self):
        return Product.objects.filter(brand__pk=self.kwargs.get("pk"), orders=self.kwargs.get("orders"))


class BrandListView(ListAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer


class CategoryListView(ListAPIView):
    permission_classes = [IsSuperUser]
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ProductListView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
