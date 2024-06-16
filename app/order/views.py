# DRF imports
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.http import HttpResponse
from rest_framework.decorators import action
from rest_framework.status import (
    HTTP_200_OK,
    HTTP_201_CREATED,
    HTTP_400_BAD_REQUEST
)

# import serializers
from order.serializers import CreateUpdateBasketSerializer

# import Redis actions
from order.redis_actions import redis_add_to_basket

# import Swagger schemas
from order.swagger_schemas import swagger_schema_add_item_to_basket


class OrderActions(ModelViewSet):
    """
    Class for creating, updating, deleting, get
    list of product items inside basket.

    Supposed, user add items to basket firstly.
    Product items in basket project save in Redis.
    """
    serializer_class = CreateUpdateBasketSerializer
    http_method_names = ['post', 'put', 'get', 'delete']
    permission_classes = (IsAuthenticated,)

    @swagger_schema_add_item_to_basket
    @action(detail=True, methods=['post'], url_path="add_item_to_basket")
    def add_item_to_basket(self, request):
        print(request.user_id)
        """ method for saving new item and quantity in basket """
        redis_add_to_basket(
            redis_user_basket_key=request.user_id,
            product_id=str(1),
            quantity=str(1)
        )
        return Response(
            status=HTTP_200_OK
        )