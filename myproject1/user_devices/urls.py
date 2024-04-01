from django.urls import path
from .views import register_admin

urlpatterns = [
    path('admin_devices/register', register_admin),
]