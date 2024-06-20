# DRF imports
from rest_framework import serializers

# import models
from product.models import Product


class GetProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        exclude = ["created", "updated"]
