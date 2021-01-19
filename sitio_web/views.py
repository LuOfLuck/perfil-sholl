from django.http import HttpResponse
from django.shortcuts import render, redirect
from servicios.models import Servicio
from .forms import Registro
from django.contrib.auth import login, authenticate
from django.contrib import messages

def Home(request):

    titulo = "home"

    return render(request, "sitio_web_app/home.html", {"titulo":titulo})



def Registro_usuarios(request):

    if request.method == "POST":
        formulario = Registro(request.POST)
        if formulario.is_valid():
            formulario.save()
            username = formulario.cleaned_data['username']
            messages.success(request, f'usuario {username} creado')
            #username = formulario.cleaned_data['username']
            #password = formulario.cleaned_data['password1s']
            #user = authenticate(username=username, password= password)
            #login(request, user)
            return redirect(to='Home')
        else:
            messages.success(request, f'No se ah podido guardar el registro')
    formula = Registro()
    return render(request, "registration/registro.html", {"from": formula})

def applicado2(request):
    return render(request, "sitio_web_app/applica2.html")