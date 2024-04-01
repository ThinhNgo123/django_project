from django.db import models
from user_devices.models import UserDevices
# Create your models here.
class ThietBi(models.Model):
    ETH_MAC = models.CharField(max_length=100)
    user_id = models.ForeignKey(UserDevices, on_delete=models.CASCADE)
