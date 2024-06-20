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


swagger_schema_create_update_basket = extend_schema(
        tags=["Order"],
        summary="Push new product item to Redis basket",
        description='POST request to push new product item to Redis basket',
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


swagger_schema_create_order = extend_schema(
        tags=["Order"],
        summary="Buy products from Redis basket",
        description='POST request to buy products from Redis basket',
        operation_id="Buy products from Redis basket",
        request=None
    )

swagger_schema_get_basket = extend_schema(
        tags=["Order"],
        summary="Get list of products from basket",
        description='GET request to get list of products from basket',
        operation_id="Get list of products from basket",
        request=None
    )


swagger_schema_delete_basket_item = extend_schema(
        tags=["Order"],
        summary="Delete product from basket",
        description='DELETE request to remove product from Redis basket',
        operation_id="Delete product from basket",
        request={
            "application/json": {
                "description": "Delete product from basket",
                "type": "object",
                "properties": {
                    "product": {
                        "type": "integer",
                    }
                },
                "required": [
                    "product"
                ],
            }
        }
    )


swagger_schema_get_orders = extend_schema(
        tags=["Order"],
        summary="Get list of orders",
        description='Get request to get list of orders',
        operation_id="Get list of orders",
    )
