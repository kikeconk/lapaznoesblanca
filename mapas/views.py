from django.shortcuts import render
from .models import MapaSocial

def index(request):
    try:
        # Traemos todos los mapas de la base de datos
        mapas = MapaSocial.objects.all()
    except Exception:
        # Si la tabla aún no existe en Render, evitamos que la página se caiga
        mapas = None
        
    # Volvemos a 'index.html' que es la ruta que Django sí reconocía
    return render(request, 'index.html', {'mapas': mapas})