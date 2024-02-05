from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .models import acciones, persona
def home(request):
    return http.HttpResponse("Página Raiz del proyecto")
def index(request):
    #return HttpResponse("<h1>Index de Acciones</h1>")
    x=5
    return render(request, 'acciones/base.html', {'x': x})

def lista_acciones(request):
    #return HttpResponse("<h1>Lista de acciones</h1>")
    Lacciones = acciones.objects.all().order_by('prioridad')
    return render(request, 'acciones/ListaAcciones2.html', {'Lacciones': Lacciones})

def accion_numero(request, id):
    return HttpResponse("<h1>Acción #"+str(id)+"</h1>")

def accion_nombre(request, nombre):
    return HttpResponse("<h1>Acción con slug "+ nombre+ "</h1>")
