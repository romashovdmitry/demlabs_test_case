""" admin interface setup """
# Django imports
from django.contrib import admin
from django import forms

# import models
from product.models.product import Product
from django.db import models


class ProductAdmin(admin.ModelAdmin):
    pass


admin.site.register(Product, ProductAdmin)
