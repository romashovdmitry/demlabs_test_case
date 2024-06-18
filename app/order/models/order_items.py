# Django imports
from django.db import models

# import models, base model for inheritance
from user.models.user import User
from product.models.product import Product
from order.models.orders import Order

# import constants
from order.constants import REDIS_PRODUCT_BASKET_NOUNT_TEMPLATE, REPLACE_KEY

# import custom foos, classes
from main.utils import redis_con


class OrderItems(models.Model):
    """
    Order items model.
    Save here choosen by user products, quantity of products
    in basket.
    """

    class Meta:
        verbose_name = "OrderItem"
        verbose_name_plural = "OrderItem"
        db_table = "order_items"

    user = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        help_text="User who buy products",
        verbose_name="User who buy products"
    )

    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        null=True,
        help_text="Purchased product",
        verbose_name="Purchased product"
    )

    quantity = models.PositiveIntegerField(
        default=1,
        help_text="How much product items was in order",
        verbose_name="How much product items was in order"
    )

    purchase_price = models.PositiveIntegerField(
        help_text="How much paid user for one product item on pruchase moment",
        verbose_name="How much paid user for one product item on pruchase moment"
    )

    order = models.ForeignKey(
        Order,
        on_delete=models.CASCADE,
        null=True
    )

    @staticmethod
    def create_order_items(
        user: User,
        order: Order,
        basket_items: list[dict],  
    ):
        for basket in basket_items:
            redis_con.hdel(
                REDIS_PRODUCT_BASKET_NOUNT_TEMPLATE.replace(
                    REPLACE_KEY, str(basket["product"])
                ),
                user.pk
            )
            OrderItems.objects.create(
                product=Product.objects.get(pk=basket["product"]),
                quantity=basket.get("quantity"),
                purchase_price=basket.get("purchase_price"),
                order=order
            )