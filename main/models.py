from django.db import models

class Logger(models.Model):
    request_ip = models.CharField(max_length=255)
    request_data = models.CharField(max_length=255)
    is_valid = models.BooleanField()
    time = models.DateTimeField(auto_now_add=True)
