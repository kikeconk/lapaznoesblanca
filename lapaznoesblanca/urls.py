from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from mapas import views

urlpatterns = [
    path('admin/', admin.site.split if hasattr(admin.site, 'split') else admin.site.urls),
    path('', views.index, name='index'), # La raíz ahora cargará tus mapas
]

# Esto le permite a Django local leer tus JPGs de la carpeta media
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)