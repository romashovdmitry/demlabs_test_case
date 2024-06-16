# Django imports
from django.urls import path

# custom DRF classes imports
from product.views import ProductsAPIView

product_list = ProductsAPIView.as_view({"get": "product_list"})
product_detail = ProductsAPIView.as_view({"get": "product_detail"})

urlpatterns = [
    path('product_detail/<int:pk>', product_detail, name='product_detail'),
    path('produict_list', product_list, name="product_list")
]