# Django imports
from django.urls import path

# import views
from order.views import OrderActions

basket_actions = OrderActions.as_view({"post": "add_item_to_basket"})

urlpatterns = [
    # for docker health-checker
    path('basket/', basket_actions, name="basket_actions"),
]