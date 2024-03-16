# products/urls.py
from django.urls import path
from .views import get_products, add_product, signup, logout_user, login_user, get_csrf_token

urlpatterns = [
    path('products/', get_products, name='get_products'),
    path('products/add', add_product, name='add_product'),
    path('products/signup', signup, name='signup'),
    path('products/logout', logout_user, name='logout'),
    path('products/login', login_user, name='login'),
    path('products/token', get_csrf_token, name='csrf token')
]
