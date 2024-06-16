"""
constant data for order app foos, models, services
"""
NEW = 0  # user add to busket but haven't pay yet
PACKED = 1  # user pai
DELIVERED = 2
CANCELED = 3

ORDER_STATUS = (
    (NEW, "NEW"),
    (PACKED, "PACKED"),
    (DELIVERED, "DELIVERED"),
    (CANCELED, "CANCELED")
)


redis_basket_template = lambda product_id=None, quantity=None: {
    'product_id': str(product_id) if product_id else "", 
    'quantity': str(quantity) if quantity else ""
}