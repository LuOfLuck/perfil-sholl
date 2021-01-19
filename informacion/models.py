from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Categoria(models.Model):

    nombre = models.CharField(max_length=50) 

    created = models.DateField(auto_now_add=True)

    update = models.DateField(auto_now_add=True)

    class Meta():
        verbose_name = "categoria"
        verbose_name_plural = "categorias"

    def __str__(self):
        return self.nombre

class Post(models.Model):
    titulo = models.CharField(max_length=40) 

    contenido = models.TextField()

    imagen = models.ImageField(upload_to="post", null=True, blank=True)

    autor = models.ForeignKey(User, on_delete = models.CASCADE)

    created = models.DateField(auto_now_add=True)

    categorias = models.ManyToManyField(Categoria)

    update = models.DateField(auto_now_add=True)

    class Meta():
        verbose_name = "post"
        verbose_name_plural = "posts"

    def __str__(self):
        return self.titulo

class Comentario(models.Model):

    contenido = models.TextField(max_length=50) 

    autor = models.ForeignKey(User, on_delete = models.CASCADE, null=True, blank=True )

    created = models.DateField(auto_now_add=True)

    id_post = models.IntegerField(null=True, blank=True )

    class Meta():
        verbose_name = "comentario"
        verbose_name_plural = "comentarios"


    def __str__(self):
        return self.contenido
