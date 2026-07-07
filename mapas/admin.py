from django.contrib import admin
from .models import MapaSocial

@admin.register(MapaSocial)
class MapaSocialAdmin(admin.ModelAdmin):
    # Columnas que se verán en la lista de mapas
    list_display = ('ano', 'departamento', 'municipio', 'coautores')
    # Filtros laterales para buscar rápido
    list_filter = ('ano', 'departamento')
    # Buscador por texto
    search_fields = ('municipio', 'contexto_historico')
