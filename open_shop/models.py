import uuid

from django.db import models


class Product(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, unique=True,
                          editable=False)
    name = models.CharField(max_length=100, error_messages={
        "blank": "Product name is required.",
        "max_length": "Product name must not exceed 100 characters."
    })
    shop = models.CharField(max_length=50, error_messages={
        "blank": "Shop name is required.",
        "max_length": "Shop name must not exceed 50 characters."
    })
    price = models.PositiveIntegerField(error_messages={
        "invalid": "Price must be greater than zero."
    })
    sku = models.CharField(max_length=20, error_messages={
        "blank": "SKU is required.",
        "max_length": "SKU must not exceed 20 characters."
    })
    description = models.TextField(error_messages={
        "blank": "Product description is required."
    })
    location = models.CharField(max_length=50, error_messages={
        "blank": "Product location is required.",
        "max_length": "Location must not exceed 50 characters."
    })
    category = models.CharField(max_length=50, error_messages={
        "blank": "Category is required.",
        "max_length": "Category must not exceed 50 characters."
    })
    stock = models.PositiveIntegerField(error_messages={
        "invalid": "Stock must be zero or greater."
    })
    is_available = models.BooleanField(default=False)
    picture = models.URLField(max_length=500, error_messages={
        "invalid": "Picture must be a valid URL.",
        "max_length": "Picture URL must not exceed 500 characters."
    })

    def __str__(self):
        return self.name
