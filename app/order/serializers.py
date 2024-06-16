# DRF imports
from rest_framework import serializers

# import models
from product.models import Product
from order.models import OrderItems, Order


class CreateUpdateBasketSerializer(serializers.ModelSerializer):

    class Meta:
        model = OrderItems
        fields = (
            "product",
            "quantity",
            "purchase_price"
        )

    def validate_product(self, object):
        pass