from django.db import models
from fairManagement.models import FairRegistration

class QR(models.Model):
   id = models.AutoField(primary_key = True)
   registration = models.ForeignKey(FairRegistration, on_delete=models.CASCADE)
   isRead = models.BooleanField(default=False)

   def set_as_read(self):
      self.isRead = True
      self.save()

   def __str__(self):
      return f"{self.id} - {self.isRead}"