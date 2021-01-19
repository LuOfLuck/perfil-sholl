from django.shortcuts import render
from .models import Producto, Compras
from django.http import JsonResponse
import json

# Create your views here.

def tienda(request):
    titulo ="Tienda"
    produto = Producto.objects.all()
    return render(request, 'tienda/tienda.html', {'producto':produto, "titulo":titulo})

def compra(request, id_producto):

    producto = Producto.objects.get(id=id_producto)

    return render(request, 'tienda/compra.html', {'producto':producto, "titulo":producto.nombre})

def completado(request):
    body = json.loads(request, body)
    print('BODY:', body)
    return JsonResponse('pago completado', safe = False)
