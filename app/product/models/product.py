# Django imports
from typing import Iterable
from django.db import models
from os import getenv

# import constants
from product.constants import ProductCategories
from order.constants import REDIS_PRODUCT_BASKET_NOUNT_TEMPLATE, REPLACE_KEY

# import base model for inheritance, etc models
from main.base_model import BaseModel
from user.models.user import User

# import custom foos, classes
from main.utils import (
    define_image_file_path,
    image_file_extension_validator

)
from main.utils import redis_con


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

    def get_redis_reserved_mount(self, previous_quantity: int):
        """ return how much product items are not free for order now """
        reservations = redis_con.hgetall(f"product_id:{self.pk}")

        return sum(
            int(quantity.decode('utf-8')) for quantity in reservations.values()
        ) - previous_quantity if reservations else 0

    def setup_redis_reserved_mount_by_user(
        self,
        items_quantity: int,
        user_id: User.pk,
        previous_quantity: int
    ):
        """
        #FIXME: другой докстринг. надо исправить.
        Update reserved mount method that used when user
            add product items to basket. Need it to
            control real mount of product on stocks
            and product reservation.

        Parameters:    
            items_quantity (int): hou much items user update in basket
            plus (bool): False - decrease value, True - increase value    
        """

        with redis_con.pipeline() as pipe:
            pipe.multi()
            redis_key = REDIS_PRODUCT_BASKET_NOUNT_TEMPLATE.replace(REPLACE_KEY, str(self.pk))
            pipe.hdel(redis_key, user_id)
            pipe.hset(redis_key, user_id, items_quantity)
            pipe.expire(redis_key, getenv("REDIS_BASKET_TIME", 100))
            pipe.execute()

