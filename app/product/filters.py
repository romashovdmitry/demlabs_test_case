# django-filters package import
from django_filters import rest_framework as filters

# import models
from .models import Product


class ProductFilter(filters.FilterSet):
    """ class for filtering requests to product DRF API  """
    category = filters.NumberFilter(field_name='category')

    class Meta:
        model = Product
        fields = ['category']