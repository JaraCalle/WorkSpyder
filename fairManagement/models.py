from django.db import models
from exploreFairs.models import JobFair

# Create your models here.
class Aspirant(models.Model):
    aspirantId = models.IntegerField(primary_key = True)
    firsrtName = models.CharField(max_length=50)
    secondName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=100)
    email = models.EmailField(max_length=255)
    phone = models.CharField(max_length=10)

class FairRegistrations(models.Model):
    registryId = models.IntegerField(primary_key = True)
    aspirant = models.ForeignKey(Aspirant, on_delete=models.CASCADE)
    fair = models.ForeignKey(JobFair, on_delete=models.CASCADE)
    registryDate = models.DateField()