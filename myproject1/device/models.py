from django.db import models
from thiet_bi.models import ThietBi

# Create your models here.
class Device(models.Model):
    device_id = models.ForeignKey(ThietBi, on_delete=models.CASCADE)
    # ID = models.CharField(max_length=100)
    sub_ID = models.CharField(max_length=100)
    location_x = models.CharField(max_length=100)
    location_y = models.CharField(max_length=100)
    area = models.CharField(max_length=100)
    province = models.CharField(max_length=100)
    time_zone = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    station = models.CharField(max_length=100)