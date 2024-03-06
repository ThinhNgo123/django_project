from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

# Create your views here.
# products/views.py
import sys
from django.http import JsonResponse
from .models import Customer
# from ..functions.math.math import function_sum

def get_products(request):
    customer = list(Customer.objects.values())
    return JsonResponse(customer, safe=False)

def add_product(request):
    if request.method == 'POST':
        data = request.POST
        customer = Customer.objects.create(
            name=data['name'],
            price=data['price']
        )
        return JsonResponse({'message': 'Customer added successfully'})

def example_api(request):
    return JsonResponse({"hello": "xin chao"})
