# DRF imports
from rest_framework import serializers
import json

# import models
from product.models import Product
from order.models import OrderItems, Order

# import constants
from order.constants import TOO_MUCH_QUANTITY
from main.utils import (
    define_user_basket_key,
    redis_decode_list,
    redis_con
)


class CreateUpdateBasketSerializer(serializers.ModelSerializer):

    product = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all())
    user_id = serializers.IntegerField()

    class Meta:
        model = OrderItems
        fields = (
            "product",
            "quantity",
            "purchase_price",
            "user_id"
        )

    def validate(self, attrs):
        """
        1. Just to change product field in serializer validated data.
        2. Check if there is enough free product's
            quantity to add it to basket.
        """
        data = super().validate(attrs)
        data["previous_basket_product"] = {}
        previous_quantity = 0

        redis_user_basket_key = define_user_basket_key(data["user_id"])
        basket_items = redis_decode_list(
            redis_con.lrange(
                    redis_user_basket_key, 0, -1
                )
            )
        # remove previouse values for quantity and price
        # if product already exists for user
        if basket_items:

            for item in basket_items:

                if item["product"] == data["product"].pk:

                    previous_quantity = item["quantity"]
                    # remove later in redis pipeline atomically (ACID)
                    # at that moment fix
                    data["previous_basket_product"] = item

        # data["quantity"] = in user's purchase
        # data["product"].get_redis_reserved_mount() = reserved in moment
        # data["product"].mount = on stock
        reseved_in_moment = data["product"].get_redis_reserved_mount(previous_quantity)
        free_to_order_in_moment = data["product"].mount - reseved_in_moment

        if data["quantity"] > (
            free_to_order_in_moment
        ):

            raise serializers.ValidationError(
                TOO_MUCH_QUANTITY.replace(
                    "<QUANTITY>", str(
                        free_to_order_in_moment
                    )
                )
            )

        data["product_object"] = data["product"]
        data["product"] = data["product"].pk

        return data


class GetOrdersSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        exclude = ["user"]
