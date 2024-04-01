from django.shortcuts import render

# Create your views here.
# products/views.py
import sys, json, datetime
from myproject1.settings import SIMPLE_JWT
from django.middleware.csrf import get_token 
from django.http import JsonResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password, check_password
# from rest_framework.decorators import api_view
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework.status import HTTP_201_CREATED, HTTP_400_BAD_REQUEST
# from .serializers import ProductSerializer
from .models import Product
from .authentications import authenticate_token, token_destroy, get_security
import jwt
from rest_framework_simplejwt.tokens import RefreshToken
# from ..functions.math.math import function_sum
# from .task import add

@authenticate_token
def get_products(request):
    if request.user.is_authenticated:
        products = Product.objects.filter(user=request.user)
        products_dict = {}
        for product in products:
            products_dict[product.name] = {"price": product.price}
        return JsonResponse(products_dict, safe=False)
    else:
        return JsonResponse("ban chua dang nhap", safe=False)

# @login_required
# @api_view(['POST'])
@authenticate_token
def add_product(request):
    if request.method == 'POST':
        # data = request.POST
        print(request.user)
        data = json.loads(request.body)
        print(data)
        # if not product.is_valid():
            # return JsonResponse("them san pham that bai", safe=False)
        Product.objects.create(
            name=data['name'],
            price=data['price'],
            user=request.user
        )
        return JsonResponse({'message': 'Them san pham thanh cong'})

# @api_view(['POST']) #decorator use request.data
def signup(request):
    if request.method == "POST":
        data = json.loads(request.body)
        username = data["username"]
        raw_password = data["password"]
        email = data["email"]
        if User.objects.filter(username=username).exists():
            return JsonResponse("Tai khoan da ton tai", safe=False)
        hash_password = make_password(raw_password)
        if not check_password(raw_password, hash_password):
            return JsonResponse("Tao tai khoan that bai", safe=False)
        user = User(
            username=username, 
            password=hash_password, 
            email=email,
            is_staff=True,
            is_active=True)
        user.save()
        # User.objects.create()
        # User.objects.create_user()
        # login(request, user)
        return JsonResponse("Tai khoan duoc tao thanh cong", safe=False)

@authenticate_token
def logout_user(request):
    if request.user.is_authenticated:
        logout(request)
        token_destroy(request)
        return JsonResponse("dang xuat thanh cong", safe=False)
    else:
        return JsonResponse("ban chua dang nhap", safe=False)

# @api_view(['POST']) #decorator use request.data
def login_user(request):
    if request.method == "POST":
        # print(request.data)
        data = json.loads(request.body)
        # print(request.body)
        user = authenticate(request, username=data["username"], password=data["password"])
        if user:
            login(request, user)
            # token, is_created = Token.objects.get_or_create(user=user)
            time = datetime.datetime.now()#.timestamp()
            # print("second:", type(time + SIMPLE_JWT["ACCESS_TOKEN_LIFETIME"]))
            print("second1:", time + SIMPLE_JWT["ACCESS_TOKEN_LIFETIME"])
            print(request.COOKIES)
            token = jwt.encode({
                'username': user.get_username(),
                'security': get_security(),
                # 'session': request.COOKIES["sessionid"] + str(time),
                'exp': (time + SIMPLE_JWT["ACCESS_TOKEN_LIFETIME"]).timestamp()
                }, key='secret_key', algorithm="HS256")
            return JsonResponse({
                "status": "dang nhap thanh cong",
                "token": token
            }, safe=False) 
        else:
            return JsonResponse("dang nhap that bai", safe=False)
    # return JsonResponse("Khong co api loai %s" %(request.method), safe=False)

def get_csrf_token(request):
    # print(request.COOKIES["sessionid"])
    # print(request.COOKIES["csrftoken"])
    return JsonResponse({"csrf_token": get_token(request)})