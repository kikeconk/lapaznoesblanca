
import os
import random
from django.shortcuts import render
from django.conf import settings

def vista_mapas(request):
    ruta_mapas = os.path.join(settings.BASE_DIR, 'media', 'mapas_jpg')
    lista_mapas = []
    
    # Lista de tamaños estéticos para el mosaico
    tamaños_disponibles = ['mapa-grande', 'mapa-mediano', 'mapa-pequeño']
    
    if os.path.exists(ruta_mapas):
        for archivo in os.listdir(ruta_mapas):
            if archivo.endswith(('.jpg', '.jpeg', '.png', '.JPG', '.JPEG', '.PNG')):
                # 1. Limpiamos el nombre del archivo usando el texto puro
                nombre_bonito = archivo.split('.')[0].replace('_', ' ')
                
                # 2. Armamos el diccionario final combinando la ruta, el nombre y el tamaño al azar
                mapa_dict = {
                    'archivo': archivo,
                    'nombre': nombre_bonito,
                    'clase_tamaño': random.choice(tamaños_disponibles)
                }
                lista_mapas.append(mapa_dict)
        
        # 3. Desordenamos la lista completa de forma aleatoria (Alineado fuera del ciclo for)
        random.shuffle(lista_mapas)

    return render(request, 'index.html', {'mapas': lista_mapas})