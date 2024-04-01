from django.db import models
from thiet_bi.models import ThietBi
# Create your models here.
class FTPServers(models.Model):
    device_id = models.ForeignKey(ThietBi, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    status = models.CharField(max_length=100)
    activate = models.CharField(max_length=100)
    ip = models.CharField(max_length=100)
    port = models.CharField(max_length=100)
    user = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    folder = models.CharField(max_length=100)
    sub_folder_format = models.CharField(max_length=100)
    send_time = models.IntegerField()
    check_activation = models.CharField(max_length=100)
    check_time = models.IntegerField()
    file_name = models.CharField(max_length=100)
    time_out = models.IntegerField()
    round_decimal = models.IntegerField()
    FTP_method = models.CharField(max_length=100)

class FTPServerFileList(models.Model):
    FTP_server_id = models.ForeignKey(FTPServers, on_delete=models.CASCADE)
    activate = models.CharField(max_length=100)
    province_code = models.CharField(max_length=100)
    company_code = models.CharField(max_length=100)
    station_code = models.CharField(max_length=100)
    folder = models.CharField(max_length=100)
    sensor_list = models.CharField(max_length=100)