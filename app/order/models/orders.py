# Django imports
from django.db import models

# import models
from user.models.user import User

# import constants
from order.constants import OrderStatus


class Order(models.Model):
    """
    Order model.
    Save here orders of user, status of orders.
    Store here history of orders.
    """

    class Meta:
        verbose_name = "Order"
        verbose_name_plural = "Orders"
        db_table = "orders"

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    sum = models.PositiveIntegerField(
        default=0,
        help_text="Sum that was paid by user for order",
        verbose_name="Sum that was paid by user for order"
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        blank=False,
        help_text="Date, time when order was placed, finished.",
        verbose_name="Date, time when order was placed, finished."
    )
    delivery_status = models.CharField(
        choices=OrderStatus,
        default=0,
        max_length=32,
        blank=False,
        verbose_name="Delivery Status",
        help_text="Delivery Status"
    )

    @staticmethod
    def create_new_order(
        user: User,
        sum: int

    ): # -> Order
        return Order.objects.create(
            user=user,
            sum=sum
        )
