from django.shortcuts import render

# Create your views here.
# products/views.py
import sys
from django.http import JsonResponse
from django.db import models, connection
from django.db.models.base import ModelBase
from .models import Product
# from ..functions.math.math import function_sum
# from .task import add

def get_products(request):
    products = list(Product.objects.values())
    return JsonResponse(products, safe=False)

def add_product(request):
    if request.method == 'POST':
        data = request.POST
        product = Product.objects.create(
            name=data['name'],
            price=data['price']
        )
        return JsonResponse({'message': 'Product added successfully'})

def example_api(request):
    # print(add.delay(4, 4))   
    return JsonResponse({'status': "Processing..."})
