"""
constant data for order app foos, models, services
"""
# Django imports
from django.db import models

# import constants
from main.constants import REPLACE_KEY

NEW = 0  # user add to busket but haven't pay yet
PACKED = 1  # user pai
DELIVERED = 2
CANCELED = 3


class OrderStatus(models.IntegerChoices):
    NEW = 0, 'NEW'
    DELIVERED = 1, 'DELIVERED'

REDIS_USER_BASKET_KEY_TEMPLATE = f"basket:user:{REPLACE_KEY}"
REDIS_PRODUCT_BASKET_NOUNT_TEMPLATE = f"product_id:{REPLACE_KEY}"

redis_basket_template = lambda product=None, quantity=None, purchase_price=None: {
    'product': str(product) if product else "", 
    'quantity': str(quantity) if quantity else "",
    "purchase_price": str(purchase_price) if purchase_price else ""
}


#errors
TOO_MUCH_QUANTITY = (
    "There is no so much product items in stock. "
    "Store has <QUANTITY> product items"
)