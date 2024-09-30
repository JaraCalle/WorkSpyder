from django.db import models
from fairManagement.models import FairRegistration

class QR(models.Model):
   id = models.AutoField(primary_key = True)
   registration = models.ForeignKey(FairRegistration, on_delete=models.CASCADE)
   isRead = models.BooleanField(default=False)