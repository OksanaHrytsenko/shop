from django.urls import include, path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions, routers

from api.views import (BrandListView, CategoryListView, CustomerViewSet,
                       ProductDetailView, ProductListView)

app_name = "api"
router = routers.DefaultRouter()
router.register("customers", CustomerViewSet)

schema_view = get_schema_view(
    openapi.Info(
        title="Product API",
        default_version="v1.0",
        description="API for product ",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="admin@admin.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path("", include(router.urls)),
    path("auth/", include("djoser.urls.jwt")),
    path("docs/", schema_view.with_ui("swagger", cache_timeout=0), name="swagger_docs"),
    path("brand/<int:pk>/brand/<int:orders>/", ProductDetailView.as_view(), name="product_detail"),
    path("brand/", BrandListView.as_view(), name="brand_list"),
    path("category/", CategoryListView.as_view(), name="category_list"),
    path("product/", ProductListView.as_view(), name="product_list"),
]
