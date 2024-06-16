# DRF imports
from rest_framework.permissions import IsAuthenticated

# Swagger imports
from drf_spectacular.utils import (
    extend_schema,
    extend_schema_view,
    OpenApiParameter,
    OpenApiExample,
    OpenApiResponse
)
from drf_spectacular.types import OpenApiTypes


swagger_schema_add_item_to_basket = extend_schema(
        tags=["Order"],
        summary="Push new product item to Redis basket",
        description='POST request to push new product item to Redis basket',
#        auth=IsAuthenticated,
        operation_id="Push new product item to Redis basket",
        # NOTE: можно добавить больше в responses, если будет время
        request={
            "application/json": {
                "description": "Product added to basket by user",
                "type": "object",
                "properties": {
                    "product": {
                        "type": "integer",
                    },
                    "quantity": {
                        "type": "integer",
                    },
                    "purchase_price": {
                        "type": "integer"
                    }
                },
                "required": [
                    "product",
                    "quantity",
                    "purchase_price"
                ],
            }
        },
        responses={
            200,
        }
    )
