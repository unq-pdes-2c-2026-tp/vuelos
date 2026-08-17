from django.db import models


class Vuelo(models.Model):
    aerolínea = models.CharField(max_length=50)
    fecha = models.DateField()
    hora = models.TimeField()
    origen = models.CharField(max_length=50)
    destino = models.CharField(max_length=50)
    capacidad = models.PositiveSmallIntegerField()
    disponibilidad = models.PositiveSmallIntegerField()
