
# DRF imports
from rest_framework.mixins import (
    ListModelMixin,
    RetrieveModelMixin
)
from rest_framework.viewsets import GenericViewSet
from rest_framework.permissions import AllowAny
from rest_framework.parsers import MultiPartParser
from rest_framework.decorators import action
from django_filters import rest_framework as filters

# Swagger imports, import Swagger custom schemas
from drf_spectacular.utils import extend_schema
from product.swagger_schemas import (
    swagger_schema_product_detail,
    swagger_schema_prduct_list
)

# import serializers
from product.serializers import GetProductSerializer

# import filters
from django_filters.rest_framework import DjangoFilterBackend
from product.filters import ProductFilter

# import models
from product.models.product import Product


class ProductsAPIView(
    ListModelMixin,
    RetrieveModelMixin,
    GenericViewSet
):
    """
    Class for retrive products.
    Could be used by client in interface to see
    products.
    """
    parser_classes = (MultiPartParser,)
    http_method_names = ['get']
    lookup_field = 'pk'
    permission_classes = [AllowAny]
    queryset = Product.objects.all()
    serializer_class = GetProductSerializer
    # https://django-filter.readthedocs.io/en/stable/guide/rest_framework.html#adding-a-filterset-with-filterset-class
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = ProductFilter

    @swagger_schema_product_detail
    @action(detail=True, methods=['get'], url_path="product_detail")
    def product_detail(self, request, *args, **kwargs):
        """ get certain product by ID """
        return super().retrieve(request, *args, **kwargs)

    @swagger_schema_prduct_list
    @action(detail=True, methods=['get'], url_path="product_list")    
    def product_list(self, request, *args, **kwargs):
        """ get all products or filtered list of products """
        return super().list(request, *args, **kwargs)
