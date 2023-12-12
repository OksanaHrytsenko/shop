from django.forms import ModelForm

from product.models import Brand, Category, Product


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ("category", "brand", "title", "price")


class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = ("name",)


class BrandForm(ModelForm):
    class Meta:
        model = Brand
        fields = ("name_brand", "country_of_brand")
