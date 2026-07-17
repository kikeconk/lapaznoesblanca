from django.urls import path
from . import views

urlpatterns = [
    path('', views.vista_mapas, name='vista_mapas'),
]