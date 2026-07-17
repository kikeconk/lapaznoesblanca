
import os
import random
from django.shortcuts import render
from django.conf import settings

def vista_mapas(request):
    # 1. Ruta exacta de la carpeta dentro de tu directorio media
    ruta_mapas = os.path.join(settings.BASE_DIR, 'media', 'mapas_jpg')
    lista_mapas = []
    
    # 2. Validar que la carpeta exista antes de leerla
    if os.path.exists(ruta_mapas):
        for archivo in os.listdir(ruta_mapas):
            if archivo.endswith(('.jpg', '.jpeg', '.png', '.JPG', '.JPEG', '.PNG')):
                lista_mapas.append(archivo)
                
        # 3. ¡El truco mágico! Desordenar la lista de forma aleatoria en cada recarga
        random.shuffle(lista_mapas)
        
        # 4. Crear una estructura con tamaños variados (Grandes, Medianos, Pequeños)
        # Definimos clases estéticas de Bootstrap o CSS personalizado
        tamaños_disponibles = ['mapa-grande', 'mapa-mediano', 'mapa-pequeño']
        
        for img in imagenes:
            lista_mapas.append({
                'url': f"{settings.MEDIA_URL}mapas_jpg/{img}",
                'nombre': img.split('.')[0].replace('_', ' '), # Limpia el nombre para mostrarlo bonito
                'clase_tamaño': random.choice(tamaños_disponibles) # Asigna un tamaño al azar
            })

    return render(request, 'index.html', {'mapas': lista_mapas})