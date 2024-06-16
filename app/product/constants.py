"""
constant data for product app foos, models, services
"""
from django.db import models


class ProductCategories(models.IntegerChoices):
    NO_CATEGORY = 0, 'NO_CATEGORY'
    SMARTPHONE = 1, 'SMARTPHONE'
    LAPTOP = 2, 'LAPTOP'
