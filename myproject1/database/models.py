from django.db import models
from thiet_bi.models import ThietBi
# Create your models here.
class Database(models.Model):
    device_id = models.ForeignKey(ThietBi, on_delete=models.CASCADE)
    url = models.CharField(max_length=100)
    user = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    org = models.CharField(max_length=100)
    bucker = models.CharField(max_length=100)
    token = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    store_time = models.BigIntegerField(default=2)