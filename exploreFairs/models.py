from django.db import models
from django.contrib.auth.models import User

class JobFair(models.Model):
    organizer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='job_fairs', null=True) # PUSE COMO NULL=TRUE MIENTRAS NO TENEMOS LOGIN, RECORDAR QUITARLO DESPÚES DE QUE HAYA LOGIN
    title = models.CharField(max_length=255)
    description = models.TextField()
    event_date = models.DateField()  # Fecha en la que se realizará el evento
    location = models.CharField(max_length=255)
    keynote_speaker = models.CharField(max_length=255)
    image = models.ImageField(upload_to='fairs/images/')

    def __str__(self):
        return self.title
