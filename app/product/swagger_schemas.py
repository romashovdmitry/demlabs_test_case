# Swagger imports
from drf_spectacular.utils import (
    extend_schema,
    extend_schema_view,
    OpenApiParameter,
    OpenApiExample,
    OpenApiResponse
)
from drf_spectacular.types import OpenApiTypes

# import models
from product.models import Product


swagger_schema_product_detail = extend_schema(
        tags=["Product"],
        summary="Get product by ID",
        description='GET request to get certain product by ID',
        auth=None,
        operation_id="Get product by ID",
        # NOTE: можно добавить больше в responses, если будет время
        responses={
            200: Product,
        }
    )

swagger_schema_prduct_list = extend_schema(
        tags=["Product"],
        summary="Get all products of store",
        description='GET request to get list of products',
        auth=None,
        operation_id="Get all products of store",
        # NOTE: можно добавить больше в responses, если будет время
        responses={
            200: Product,
        },
        parameters=[
            OpenApiParameter(
                name='category',
                description='Category of product',
                required=False,
                type=int,
                examples=[
                    OpenApiExample(
                        'Category example',
                        value=1
                    ),
                ],
            ),
        ]
    )