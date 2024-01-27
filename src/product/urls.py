from django.urls import path

from product.views import BrandListView, CategoryListView, ProductListView, bitcoin, generate_products

app_name = "product"

urlpatterns = [
    path("", ProductListView.as_view(), name="get_product"),
    path("category/", CategoryListView.as_view(), name="get_category"),
    path("brand/", BrandListView.as_view(), name="get_brand"),
    path("bitcoin/", bitcoin, name="bitcoin"),
    path("create_product/", generate_products, name="create_product"),
]
