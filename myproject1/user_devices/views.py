from django.shortcuts import render
from .models import UserDevices
from django.contrib.auth.models import User
from rest_framework.decorators import api_view
from django.http.response import JsonResponse
# Create your views here.

@api_view(["POST"])
def register_admin(request):
    if request.method == "POST":
        print(request)
        new_username, new_password = request.data["username"], request.data["password"]
        user = User.objects.create_superuser(username=new_username, password=new_password)
        if user:
            return JsonResponse({"status": "ok"})
    return JsonResponse({"status": "no ok"})
