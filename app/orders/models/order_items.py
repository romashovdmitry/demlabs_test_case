# Django imports
from django.db import models

# import models
from user.models.user import User
from product.models.product import Product

# import constants


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

    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
