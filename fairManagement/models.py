from django.db import models
from django.conf import settings
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError

class Aspirant(models.Model):
    id = models.AutoField(primary_key = True)
    firstName = models.CharField(max_length=50)
    secondName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=100)
    phone = models.CharField(
        max_length=10,
        validators=[
            RegexValidator(
                regex=r'^\d{10}$',  # Expresión regular para exactamente 10 dígitos
                message="El número de teléfono debe tener exactamente 10 dígitos.",
                code='invalid_phone'
            )
        ]
    )
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=1)

    def is_aspirant_data_empty(self) -> bool:
        return self.firstName == "" or self.phone == ""

    def __str__(self):
        return f"{self.firstName} {self.secondName} {self.lastName}"


class FairRegistration(models.Model):
    id = models.AutoField(primary_key=True)
    aspirant = models.ForeignKey(Aspirant, on_delete=models.CASCADE)
    fair = models.ForeignKey('exploreFairs.JobFair', on_delete=models.CASCADE)
    registrationDate = models.DateField()

    def clean(self):
        if not self.fair.maximum_capacity:
            return
        
        if self.fair.number_of_registered >= self.fair.maximum_capacity:
            raise ValidationError("No se pueden agregar más participantes, el aforo máximo ha sido alcanzado.")

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)
        self.fair.update_number_of_registered()

    def delete(self, *args, **kwargs):
        super().delete(*args, **kwargs)
        self.fair.update_number_of_registered()

    def __str__(self):
        return f"{self.aspirant} {self.fair}"

class FairFavorite(models.Model):
    id = models.AutoField(primary_key=True)
    aspirant = models.ForeignKey(Aspirant, on_delete=models.CASCADE)
    fair = models.ForeignKey('exploreFairs.JobFair', on_delete=models.CASCADE)
    favoriteDate = models.DateField()
