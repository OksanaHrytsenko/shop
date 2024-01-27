from random import randint

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView
from faker import Faker
from webargs import fields
from webargs.djangoparser import use_args

from product.forms import BrandForm, CategoryForm
from product.models import Brand, Category, Product

from product.tasks import mine_bitcoin
class ProductListView(LoginRequiredMixin, ListView):
    model = Product
    template_name = "product/list.html"
    context_object_name = "product"
    success_url = reverse_lazy("product:get_product")

    def get_queryset(self):
        queryset = super().get_queryset()
        search_text = self.request.GET.get("search_text", "")

        if search_text:
            search_fields = [
                "title__icontains",
                "brand__icontains",
                "category__icontains",
                "price__icontains",
            ]
            or_filter = Q()

            for field in search_fields:
                or_filter |= Q(**{field: search_text})

            queryset = queryset.filter(or_filter)

        return queryset


class CategoryListView(LoginRequiredMixin, ListView):
    model = Category
    template_name = "product/list_category.html"
    context_object_name = "category"
    success_url = reverse_lazy("product:get_category")


class BrandListView(LoginRequiredMixin, ListView):
    model = Brand
    template_name = "product/list_brand.html"
    context_object_name = "brand"
    success_url = reverse_lazy("product:get_brand")


def bitcoin(request):
    mine_bitcoin.delay()
    return HttpResponse("Task is started")

@classmethod
def generate_products(cls, count):
    faker = Faker()
    for _ in range(count):
        product = Product(
                title=faker.word(),
                brand=faker.word(),
                description=faker.paragraph(nb_sentences=5),
                category=faker.word(),
                price=randint(1, 1000),
            ).save()
        return product
