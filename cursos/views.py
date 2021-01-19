from django.shortcuts import render
from cursos.models import Cursos, Materia
# Create your views here.

def cursos(request):
    materia = Materia.objects.all()
    cursos = Cursos.objects.all().order_by('año')
    titulo = "Lista de cursos"
    return render(request, "cursos/cursos.html", {"cursos":cursos, "titulo":titulo, "materia":materia,})

def materia(request, id_curso):
    titulo = "Materias"

    curso = Cursos.objects.get(id=id_curso)

    materias = Materia.objects.filter(curso=curso)

    return render(request, "cursos/materias.html", {"materias":materias,"titulo":titulo})
