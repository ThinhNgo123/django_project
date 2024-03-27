from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
# Create your models here.

class UserDevices(AbstractBaseUser, PermissionsMixin):
    role = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    area_scope = models.CharField(max_length=100)
    province_scope = models.CharField(max_length=100)