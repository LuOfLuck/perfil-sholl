from django.shortcuts import render
#from .models import Contacto
from django.contrib.auth.models import User
from .forms import Contacto_forms
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
# Create your views here.

def contacto(request):

    titulo = "contacto"

    if request.method=="POST":

        asunto = request.POST["asunto"]

        emailfrom = settings.EMAIL_HOST_USER

        emailrecipiente= ["lucas33322@gmail.com"]

        mensaje = request.POST["nombre"] + ": " + request.POST["contenido"] + " " + request.POST["email"]

        send_mail(asunto, mensaje, emailfrom, emailrecipiente)

        messages.success(request, f'mail enviado con exito')

    formulario = Contacto_forms()

    return render(request, "contacto/contacto.html", {"formulario":formulario, "titulo":titulo})