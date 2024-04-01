from django.db import models
from thiet_bi.models import ThietBi
# Create your models here.
class Connect(models.Model):
    device_id = models.ForeignKey(ThietBi, on_delete=models.CASCADE)
    activation = models.CharField(max_length=100)
    server_url = models.CharField(max_length=100)
    server_port = models.CharField(max_length=100)
    end_point = models.CharField(max_length=100)
    owner = models.CharField(max_length=100)
    owner_token = models.CharField(max_length=100)
    wan_port_web_app = models.IntegerField()
    wan_port_database = models.IntegerField()
    wan_port_api = models.IntegerField()
    wan_port_ssh = models.IntegerField()
    wan_port_modbus_tcp_ip = models.IntegerField()