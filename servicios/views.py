from django.shortcuts import render
from .models import Servicio
# Create your views here.

def Servicios(request):

    servicio = Servicio.objects.all()
    titulo = "Home"
    return render(request, "sitio_web_app/home.html", {"servicio": servicio, "titulo":titulo})
