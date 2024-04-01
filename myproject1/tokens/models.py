from django.db import models
from user_devices.models import UserDevices

# Create your models here.
class Tokens(models.Model):
    creating_date = models.DateTimeField(auto_now_add=True)
    duration = models.DurationField()
    token_string = models.CharField(max_length=500)
    user_id = models.ForeignKey(UserDevices, on_delete=models.CASCADE)