from django.shortcuts import render
from .models import MapaSocial

def index(request):
    # Traemos todos los mapas ordenados como definimos en el modelo
    mapas = MapaSocial.objects.all()
    return render(request, 'index.html', {'mapas': mapas})

from django.shortcuts import render
from .models import MapaSocial

def index(request):
    try:
        # Traemos todos los mapas de la base de datos
        mapas = MapaSocial.objects.all()
    except Exception:
        # Si la tabla aún no existe en Render, evitamos que la página se caiga
        mapas = None
        
    # Ajustamos la ruta a 'mapas/index.html' si está dentro de esa subcarpeta
    return render(request, 'mapas/index.html', {'mapas': mapas})
