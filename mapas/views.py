from django.shortcuts import render
from .models import MapaSocial

def index(request):
    # Traemos todos los mapas ordenados como definimos en el modelo
    mapas = MapaSocial.objects.all()
    return render(request, 'index.html', {'mapas': mapas})
