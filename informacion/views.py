from django.shortcuts import render, redirect
from informacion.models import Post, Categoria, Comentario
from informacion.forms import ComentarioFrom
# Create your views here.

def informacion(request):

    titulo = "blog"

    categoria = Categoria.objects.all()

    post = Post.objects.all()

    return render(request, "informacion/blog.html", {"titulo":titulo, "post":post, "categoria":categoria,})


def categoria(request, categoria_id):

    titulo = "categoria"

    id_categoria = Categoria.objects.get(id=categoria_id)

    post = Post.objects.filter(categorias=id_categoria)

    categorias = Categoria.objects.all()

    return render(request, "informacion/categoria.html", {"categoria_id":id_categoria, "post":post,"titulo":titulo, "categoria":categorias, })


def post(request, post_id):
    
    if request.method == "POST":
        ide = request.user
        contenido = request.POST['contenido']
        p = Comentario(contenido=contenido, autor=ide, id_post=post_id)
        p.save()

    comentarios = Comentario.objects.filter(id_post=post_id).order_by('-created')
    formu = ComentarioFrom()
    post = Post.objects.get(id=post_id)
    
    return render(request, "informacion/post.html", {"post":post,"titulo":post.titulo,"from":formu, "comentarios":comentarios})
