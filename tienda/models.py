from django.db import models

# Create your models here.

class Producto(models.Model):

    nombre = models.CharField(max_length=40)

    descripcion = models.TextField(max_length=400)

    imagen = models.URLField()

    precio = models.FloatField(null=True, blank=True)

    class Meta():
        verbose_name = "producto"
        verbose_name_plural = "productos"

    def __str__(self):
        return self.nombre


class Compras(models.Model):
    producto = models.ForeignKey(Producto, max_length=200, null=True, blank=True, on_delete = models.CASCADE)
    fecha = models.DateTimeField(auto_now_add=True)

    class Meta():
        verbose_name = "compra"
        verbose_name_plural = "Compras"

    def __str__(self):
        return self.producto
