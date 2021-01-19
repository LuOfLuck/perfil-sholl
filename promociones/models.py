from django.db import models
from servicios.models import Servicio

# Create your models here.

class Promocion(models.Model):
    nombre = models.CharField(max_length=20, null=True, blank=True)
    año = models.IntegerField()
    foto = models.ImageField(upload_to="fondo_promocion", null=True, blank=True)
    mensaje = models.TextField(max_length=400, null=True, blank=True)
    class Meta():
        verbose_name = "promocion"
        verbose_name_plural = "promociones"

    def __str__(self):
        return str(self.año)

class Estudiante(models.Model):

    msj = "era una persona de pocas palabras, le deseamos lo mejor"

    nombre = models.CharField(max_length=15)
    apellido = models.CharField(max_length=20)
    especialidad = models.ForeignKey(Servicio, on_delete = models.CASCADE, null=True, blank=True)
    foto = models.ImageField(upload_to="promocion", null=True, blank=True)
    mensaje = models.CharField(max_length=250, default=msj)
    promocion = models.ForeignKey(Promocion, on_delete = models.CASCADE)
    class Meta():
        verbose_name = "estudiante"
        verbose_name_plural = "estudiantes"

    def __str__(self):
        return self.nombre

class Recuerdos(models.Model):
    foto = models.ImageField(upload_to="recuerdos")
    promocion = models.ForeignKey(Promocion, on_delete = models.CASCADE)
    class Meta():
        verbose_name = "Recuerdo"
        verbose_name_plural = "Recuerdos"
