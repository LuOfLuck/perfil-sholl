from django.shortcuts import render
from .models import Promocion, Estudiante, Recuerdos
from servicios.models import Servicio
# Create your views here.

def promociones(request):

    titulo = "Promociones"

    promocion = Promocion.objects.all()
    
    return render(request, "promociones/promociones.html", {"promocion":promocion, "titulo":titulo})

def egrasados(request, año):

    titulo = "Egresados"

    año = Promocion.objects.get(año=año)

    estudiante = Estudiante.objects.filter(promocion=año)

    servicio = Servicio.objects.all()

    return render(request, "promociones/egresados.html", {"estudiantes":estudiante, "servicios":servicio, "titulo":titulo, })

def recuerdos(request, año):

    titulo = "recuerdos"

    año = Promocion.objects.get(año=año)

    foto = Recuerdos.objects.filter(promocion=año)

    return render(request, "promociones/recuerdos.html", {"foto":foto, "titulo":titulo, })