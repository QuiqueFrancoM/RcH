from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .models import personal, globos

def raiz(request):
    return HttpResponse('<h1>Raiz Cumpleaños</h1>')

def personal_list(request):
    personals = personal.objects.all()
    return render(request, 'birthdays/Cumpleañeros.html', {'personals': personals})

def personal_detail(request, id):
    person = personal.objects.get(id=id)
    return render(request, 'birthdays/CumpeañeroHoy.html', {'person': person})

def globos_dibujo(request):
    balloon = globos.objects.all()
    contador = 0
    return render(request, 'birthdays/globos.html', {'balloon': balloon, 'contador':contador})