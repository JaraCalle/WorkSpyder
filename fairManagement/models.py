from django.db import models
from django.conf import settings
from exploreFairs.models import JobFair

class Aspirant(models.Model):
    id = models.AutoField(primary_key = True)
    firsrtName = models.CharField(max_length=50)
    secondName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=100)
    email = models.EmailField(max_length=255)
    phone = models.CharField(max_length=10)
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return f"{self.firsrtName} {self.lastName}"


class FairRegistration(models.Model):
    id = models.AutoField(primary_key = True)
    aspirant = models.ForeignKey(Aspirant, on_delete=models.CASCADE)
    fair = models.ForeignKey(JobFair, on_delete=models.CASCADE)
    registrationDate = models.DateField()

    def __str__(self):
        return f"{self.aspirant} {self.fair}"