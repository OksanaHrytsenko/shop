from django.urls import path

from product.views import BrandListView, CategoryListView, ProductListView

app_name = "product"

urlpatterns = [
    path("", ProductListView.as_view(), name="get_product"),
    path("category/", CategoryListView.as_view(), name="get_category"),
    path("brand/", BrandListView.as_view(), name="get_brand"),
]
