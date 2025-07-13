from django.db import models

class ParqueNatural(models.Model):
    nombre = models.CharField(max_length=100)
    ubicacion = models.CharField(max_length=150)
    area_km2 = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.nombre

class GuiaTuristico(models.Model):
    cedula = models.CharField(max_length=10, unique=True)
    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    experiencia = models.IntegerField()
    parque = models.ForeignKey(ParqueNatural, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.nombres} {self.apellidos}"

class Recorrido(models.Model):
    nombre = models.CharField(max_length=100)
    duracion_horas = models.DecimalField(max_digits=4, decimal_places=2)
    costo = models.DecimalField(max_digits=6, decimal_places=2)
    guia = models.ForeignKey(GuiaTuristico, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre
