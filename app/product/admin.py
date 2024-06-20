""" admin interface setup """
# Django imports
from django.contrib import admin

# import models
from product.models.product import Product


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'mount')


admin.site.register(Product, ProductAdmin)
