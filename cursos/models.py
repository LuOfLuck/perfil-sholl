from django.db import models
from servicios.models import Servicio
# Create your models here.

class Cursos(models.Model):
    año = models.CharField(max_length=4)
    carga_horaria = models.IntegerField(null=True, blank=True)
    especialidad = models.ForeignKey(Servicio, on_delete = models.CASCADE, null=True, blank=True)
    ciclo_superior = models.BooleanField(null=True, blank=True)
    class Meta():
        verbose_name = "Curso"
        verbose_name_plural = "Cursos"
    def __str__(self):
        return self.año

class Materia(models.Model):
    SHIRT_SIZES = (
        ('Aula', 'Aula'),
        ('Taller', 'Taller'),
    )
    nombre = models.CharField(max_length=30)
    curso = models.ManyToManyField(Cursos)
    tipo = models.CharField(max_length=20, choices=SHIRT_SIZES)
    horas_semanales = models.IntegerField(null=True, blank=True)
    contenido = models.TextField()
    class Meta():
        verbose_name = "Materia"
        verbose_name_plural = "Materias"
    def __str__(self):
        return self.nombre