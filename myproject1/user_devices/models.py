from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, User, AbstractUser
# Create your models here.

class UserDevices(User):
    role = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    area_scope = models.CharField(max_length=100)
    province_scope = models.CharField(max_length=100)

    class Meta(AbstractUser.Meta):
        swappable = "AUTH_USER_MODEL1"

    def __str__(self) -> str:
        return self.username