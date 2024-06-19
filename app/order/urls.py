# Django imports
from django.urls import path

# import views, websocket consumers
from order.views import OrderActions

basket_crud = OrderActions.as_view(
    {
        "post": "create_update_basket",
        "get": "get_basket",
        "delete": "delete_basket_item"
    }
)
create_order = OrderActions.as_view({"post": "create_order"})

urlpatterns = [
    # for docker health-checker
    path('basket/<int:pk>', basket_crud, name="basket_crud"),
    path('create/', create_order, name="create_order")
]
