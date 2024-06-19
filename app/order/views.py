# Python imports
import asyncio

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
from order.serializers import (
    CreateUpdateBasketSerializer,
    GetBasketSerializer
)

# import Redis actions
from order.services import (
    redis_add_to_basket,
    create_order_from_basket,
    get_basket_items,
    delete_redis_product
)

# import Swagger schemas
from order.swagger_schemas import (
    swagger_schema_create_update_basket,
    swagger_schema_create_order,
    swagger_schema_get_basket,
    swagger_schema_delete_basket_item
)

# import custom foos, classes
from main.utils import foo_name
from telegram_bot.services import telegram_log_errors


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
    serializer_class = CreateUpdateBasketSerializer

    serializer_map = {
        'create_update_basket': CreateUpdateBasketSerializer,
        'get_basket': GetBasketSerializer,
    }

    def get_serializer_class(self):
        """ define serializer for class """

        return self.serializer_map[self.action]


    @swagger_schema_create_update_basket
    @action(detail=True, methods=['post'], url_path="create_update_basket")
    def create_update_basket(self, request):
        """
        1. Serizlie request.data, check if there are anough free items
            to make order
        2. Create/Update values in Redis about user basket and resevations
            of product by users
        """
        try:
            
            serializer = self.serializer_class(
                data={
                    **request.data,
                    "user_id": request.user_id
                    }
                )

            if serializer.is_valid():

                redis_add_to_basket(
                    redis_user_basket_key=request.user_id,
                    **serializer.validated_data,
                )

                return Response(
                    status=HTTP_201_CREATED
                )
        
            return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

        except Exception as ex:
            asyncio.run(
                telegram_log_errors(
                    f'[{foo_name()}]'
                    f'Ex text: {str(ex)}'
                )
            )
            return Response(
                str(ex),
                status=HTTP_400_BAD_REQUEST
            )

    @swagger_schema_create_order
    @action(detail=False, methods=['post'], url_path="create_order")
    def create_order(self, request):
        """
        1. When user is ready to pay, user request here 
        """
        create_order_from_basket(request.user)
        return Response(status=HTTP_201_CREATED)
    
    @swagger_schema_get_basket
    @action(detail=False, methods=['get'], url_path="get_basket")
    def get_basket(self, request):

        try:

            return Response(
                status=HTTP_200_OK,
                data=get_basket_items(request.user)
            )

        except Exception as ex:
            asyncio.run(
                telegram_log_errors(
                    f'[{foo_name()}]'
                    f'Ex text: {str(ex)}'
                )
            )

            return Response(
                str(ex),
                status=HTTP_400_BAD_REQUEST
            )

    @swagger_schema_delete_basket_item
    @action(detail=False, methods=['delete'], url_path="delete_basket_item")
    def delete_basket_item(self, request, pk=None):
        
        try:

            delete_redis_product(request.user_id, pk)

            return Response(status=HTTP_200_OK)

        except Exception as ex:
            asyncio.run(
                telegram_log_errors(
                    f'[{foo_name()}]'
                    f'Ex text: {str(ex)}'
                )
            )

            return Response(
                str(ex),
                status=HTTP_400_BAD_REQUEST
            )