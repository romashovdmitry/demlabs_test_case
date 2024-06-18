# Django imports
from django.urls import path

# import views, websocket consumers
from order.views import OrderActions

basket_actions = OrderActions.as_view({"post": "add_item_to_basket"})
create_order = OrderActions.as_view({"post": "create_order"})

urlpatterns = [
    # for docker health-checker
    path('basket/', basket_actions, name="basket_actions"),
    path('create/', create_order, name="create_order")
]
