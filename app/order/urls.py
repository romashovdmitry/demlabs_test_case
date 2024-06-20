# Django imports
from django.urls import path

# import views, websocket consumers
from order.views import OrderBasketActions

basket_crud = OrderBasketActions.as_view(
    {
        "post": "create_update_basket",
        "get": "get_basket"
    }
)

basket_pk_crud = OrderBasketActions.as_view(
    {
        "delete": "delete_basket_item"
    }
)

order_create = OrderBasketActions.as_view({"post": "create_order"})
order_get = OrderBasketActions.as_view({"get": "get_orders"})


urlpatterns = [
    # for docker health-checker
    path('basket/', basket_crud, name="basket_crud"),
    path('basket/<int:pk>', basket_pk_crud, name="basket_pk_crud"),
    path('', order_get, name="order_get"),
    path('create/', order_create, name="create_order")
]
