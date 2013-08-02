from django.db import models

class RequestLog(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    ip = models.IPAddressField()
    path = models.URLField()
    user_agent = models.CharField(max_length=256)

