# Django imports
from django.db import models

# import constants
from product.constants import ProductCategories

# import base model for inheritance
from main.base_model import BaseModel

# import custom foos, classes
from main.utils import (
    define_image_file_path,
    image_file_extension_validator

)


def define_product_image_path(instance, filename):

    return define_image_file_path(
        instance_indicator=str(instance.id),
        filename=filename,
        object_type="_product_image.",
        directory="product_image/"
    )


class Product(BaseModel):
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

    category = models.PositiveSmallIntegerField(
        choices=ProductCategories,
        default=0,  # no category
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

    product_image = models.ImageField(
        upload_to=define_product_image_path,
        null=True,
        verbose_name="Product Image",
        help_text="Product Image",
        validators=[image_file_extension_validator]
    )