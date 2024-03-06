from django.shortcuts import render

# Create your views here.
# products/views.py
import sys
from django.http import JsonResponse
from django.db import models, connection
from django.db.models.base import ModelBase
from .models import Product
# from ..functions.math.math import function_sum

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

import importlib

import os
def example_api(request):
    # setattr(Product, "description12", models.CharField(max_length=100))
    # os.system("python manage.py makemigrations")
    # os.system("python manage.py migrate")
    # print(Product.__dict__)
    # print(request)
    rj = {
        "column": "Description12",
        "data type": "nvarchar",
        "size": 500
    }
    print(request)
    # Product.objects.raw(
    #     "ALTER TABLE %s ADD %s %s(%s)", 
    #     [
    #         Product._meta.db_table, 
    #         rj["column"], 
    #         rj["data type"],
    #         rj["size"]
    #     ]
    # )
    Product.objects.create(name="game", price="100")
    # with connection.cursor() as cursor:
    #     cursor.execute(
    #         f"ALTER TABLE products_product ADD {request_json['column']} {request_json['data type']}({request_json['size']});")
        # cursor.execute("SELECT * FROM products_product")
    # Product.add_to_class('new field', models.CharField(max_length=100))
    # print("ok")
    # product_model = Product()
    # os.system("python manage.py makemigrations")
    # os.system("python manage.py migrate")
    # product_model.save()
    # ModelBase.__init__ = example_api
    return JsonResponse({'status': f"Add column successfully to table {Product._meta.db_table}"})
