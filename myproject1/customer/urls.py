# products/urls.py
from django.urls import path
from .views import example_api

urlpatterns = [
    path('api/customer/example', example_api, name='example_api')
]
