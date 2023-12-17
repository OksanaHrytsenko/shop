from django.contrib.auth import get_user_model
from rest_framework.serializers import ModelSerializer

from product.models import Brand, Category, Order, Product


class CustomerSerializer(ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ("id", "first_name", "last_name", "email", "is_staff")


class OrderSerializer(ModelSerializer):
    class Meta:
        model = Order
        fields = ("id", "product", "user")


class ProductSerializer(ModelSerializer):
    orders = OrderSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = ("id", "category", "brand", "title", "orders", "price", "orders")


class BrandSerializer(ModelSerializer):
    class Meta:
        model = Brand
        fields = ("id", "name_brand", "country_of_brand")


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = ("id", "name")
