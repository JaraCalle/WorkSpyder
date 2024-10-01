from django.db import models
from django.contrib.auth.models import User
from exploreFairs.models import JobFair

class Aspirant(models.Model):
    id = models.AutoField(primary_key = True)
    firsrtName = models.CharField(max_length=50)
    secondName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=100)
    email = models.EmailField(max_length=255)
    phone = models.CharField(max_length=10)
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=1)

class FairRegistration(models.Model):
    id = models.AutoField(primary_key = True)
    aspirant = models.ForeignKey(Aspirant, on_delete=models.CASCADE)
    fair = models.ForeignKey(JobFair, on_delete=models.CASCADE)
    registrationDate = models.DateField()