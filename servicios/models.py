from django.db import models

# Create your models here.

class Servicio(models.Model): 

    titulo = models.CharField(max_length=20) 

    contenido = models.TextField()

    imagen = models.ImageField(upload_to="servicios")

    created = models.DateField(auto_now_add=True)

    update = models.DateField(auto_now_add=True)

    class Meta():
        verbose_name = "servicio"
        verbose_name_plural = "servicios"

    def __str__(self):
        return self.titulo
