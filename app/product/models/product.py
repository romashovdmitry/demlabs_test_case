# Django imports
from django.db import models

# import constants
from product.constants import PRODUCT_CATEGORIES


class Product(models.Model):
    """
    Products model.
    Only shop-admin can create and update new items.
    """

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"
        db_table = "products"

    name = models.CharField(
        max_length=128,
        null=True,
        blank=False,
        verbose_name="Product Name",
        help_text="Product Name"
    )

    category = models.CharField(
        choices=PRODUCT_CATEGORIES,
        null=False,
        blank=False,
        verbose_name="Product Category",
        help_text="Product Category"
    )

    price = models.PositiveBigIntegerField(
        default=0,
        null=False,
        verbose_name="Product Price",
        help_text="Product Price"
    )

    mount = models.PositiveIntegerField(
        default=0,
        null=False,
        verbose_name="Mount of products on stock",
        help_text="Mount of products on stock"
    )

    is_active = models.BooleanField(
        default=False,
        verbose_name="Product is saling or not",
        help_text="Product is saling or not"
    )