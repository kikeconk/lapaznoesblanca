from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from mapas.views import index  # Importa tu vista principal

urlpatterns = [
    # 1. El administrador SIEMPRE debe ir primero para que Django lo reconozca de una vez
    path('admin/', admin.site.urls),
    
    # 2. Tu página principal de mapas
    path('', index, name='index'),
]

# 3. Las rutas de archivos estáticos y de Cloudinary/Media se ponen AL FINAL
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)