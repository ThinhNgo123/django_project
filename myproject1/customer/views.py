from django.shortcuts import render

# Create your views here.

# Create your views here.
# products/views.py

from django.http import JsonResponse
from .models import Customer
from functions.math.math import function_sum

def example_api(request):
    return JsonResponse({"hello": function_sum()})
