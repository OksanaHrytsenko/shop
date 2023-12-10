from django.contrib import admin

from product.models import Brand, Cart, Category, Order, Product

admin.site.register([Product, Brand, Category, Cart, Order])
