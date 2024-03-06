# products/urls.py
from django.urls import path
from .views import get_products, add_product, example_api

urlpatterns = [
    path('api/customer/', get_products, name='get_products'),
    path('api/customer/add/', add_product, name='add_product'),
    path('api/customer/example', example_api, name='example_api')
]
