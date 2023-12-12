from django.contrib.auth import get_user_model
from django.db import models


class Product(models.Model):
    category = models.ForeignKey(to="product.Category", on_delete=models.CASCADE, related_name="categores")
    brand = models.ForeignKey(to="product.Brand", on_delete=models.CASCADE, related_name="brands")
    title = models.CharField(max_length=255)
    description = models.TextField(max_length=500, blank=True, null=True)
    image = models.ImageField(default="media/product/covers/default.png", upload_to="media/product/covers")
    reviews = models.TextField(max_length=255, null=True, blank=True)
    price = models.PositiveIntegerField(null=True, blank=True)

    def __str__(self):
        return f"{self.category} {self.brand} {self.title}{self.price} ({self.id})"


class Order(models.Model):
    product = models.ForeignKey(to="product.Product", on_delete=models.CASCADE, related_name="orders")
    user = models.ForeignKey(to=get_user_model(), on_delete=models.CASCADE, related_name="orders")
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return f"{self.user.email} {self.product.title} {self.created_at}"


class Cart(models.Model):
    product = models.ForeignKey(to="product.Product", on_delete=models.CASCADE, related_name="carts")
    order_number = models.PositiveSmallIntegerField(null=True, blank=True)

    def __str__(self):
        return f"{self.product} {self.order_number}"


class Category(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        verbose_name_plural = "Categories"
        verbose_name = "Category"

    def __str__(self):
        return f"{self.name}"


class Brand(models.Model):
    name_brand = models.CharField(max_length=255, null=True)
    country_of_brand = models.CharField(max_length=255, null=True)

    def __str__(self):
        return f"{self.name_brand} {self.country_of_brand}"
