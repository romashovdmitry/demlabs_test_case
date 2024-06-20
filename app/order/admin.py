""" admin interface setup """
# Django imports
from django.contrib import admin

# import models
from order.models import Order


class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'created_at', 'delivery_status')


admin.site.register(Order, OrderAdmin)
