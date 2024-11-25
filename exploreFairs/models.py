from django.db import models
from django.conf import settings

class JobFair(models.Model):
    organizer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='job_fairs', null=True) # PUSE COMO NULL=TRUE MIENTRAS NO TENEMOS LOGIN, RECORDAR QUITARLO DESPÚES DE QUE HAYA LOGIN
    title = models.CharField(max_length=255)
    description = models.TextField()
    start_event_date = models.DateField(default="2024-09-12")
    end_event_date = models.DateField(null=True, default="2024-09-13")
    department = models.CharField(max_length=255, default="Antioquía")
    city = models.CharField(max_length=255,default="Bello")
    start_hour = models.TimeField(auto_now=False, auto_now_add=False, default="12:00:00")
    end_hour = models.TimeField(auto_now=False, auto_now_add=False, null=True, default="11:00:00")
    direction = models.CharField(max_length=255)
    keynote_speaker = models.CharField(max_length=255)
    image = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.title
