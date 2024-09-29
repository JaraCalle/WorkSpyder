from django.db import models

# Create your models here.
class Ferias(models.Model):
    tituloFeria = models.CharField(max_length=250)
    descFeria = models.CharField(max_length=1500)
    fechaFeria = models.DateField()
    lugarFeria = models.CharField(max_length=250)
    ponenteFeria = models.CharField(max_length=250)  # Eventualmente hay que agregar una FK a la base de datos de usuarios
    imagenFeria = models.ImageField()
    # no puedo poner una FK a la empresa porque esa base de datos no existe aún y eso
