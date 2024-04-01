from django.db import models
from thiet_bi.models import ThietBi
# Create your models here.
class Error(models.Model):
    device_id = models.ForeignKey(ThietBi, on_delete=models.CASCADE)
    code = models.IntegerField()
    time = models.CharField(max_length=100)
    date = models.CharField(max_length=100)
    number = models.CharField(max_length=100)
    content = models.CharField(max_length=100)