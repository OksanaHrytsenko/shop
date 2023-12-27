from product.models import Brand, Cart, Category, Product


def sample_product(title: str, **params) -> Product:
    default = {
        "description": "Some text",
        "brand": Brand.objects.create(name_brand="TestBrand"),
        "category": Category.objects.create(name="TestCategory"),
    }
    default.update(params)
    return Product.objects.create(title=title, **default)
