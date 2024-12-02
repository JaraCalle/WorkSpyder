from django.db import models
from django.conf import settings
from django.utils.timezone import now
from django.core.exceptions import ValidationError

class JobFair(models.Model):
    organizer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='job_fairs')
    title = models.CharField(max_length=255)
    description = models.TextField()
    start_event_date = models.DateField()
    end_event_date = models.DateField(null=True)
    department = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    start_hour = models.TimeField(auto_now=False, auto_now_add=False)
    end_hour = models.TimeField(auto_now=False, auto_now_add=False, null=True)
    direction = models.CharField(max_length=255)
    keynote_speaker = models.CharField(max_length=255)
    image = models.URLField(blank=True, null=True)

    def clean(self):
        # Verificar si la fecha de inicio es mayor que la fecha actual
        if self.start_event_date <= now().date():
            raise ValidationError({'start_event_date': 'La fecha de inicio debe ser mayor a la fecha actual.'})
        
        # Verificar si la fecha de fin (si se proporciona) es posterior a la fecha de inicio
        if self.end_event_date and self.end_event_date < self.start_event_date:
            raise ValidationError({'end_event_date': 'La fecha de fin debe ser posterior a la fecha de inicio.'})

    def save(self, *args, **kwargs):    
        self.clean()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
