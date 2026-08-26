from django.db import models


class Vuelo(models.Model):
    aerolinea = models.CharField(max_length=50)
    fecha = models.DateField()
    hora = models.TimeField()
    origen = models.CharField(max_length=50)
    destino = models.CharField(max_length=50)
    capacidad = models.PositiveSmallIntegerField()
    disponibilidad = models.PositiveSmallIntegerField()


class VentaVuelo(models.Model):
    vuelo = models.ForeignKey(Vuelo, on_delete=models.CASCADE)
    nombre_pasajero = models.CharField(max_length=50)
    email_pasajero = models.EmailField()
    fecha_venta = models.DateTimeField(auto_now_add=True)
