from django.db import models

class MapaSocial(models.Model):
    DEPARTAMENTOS_CHOICES = [
        ('Amazonas', 'Amazonas'),
        ('Antioquia', 'Antioquia'),
        ('Arauca', 'Arauca'),
        ('Atlantico', 'Atlántico'),
        ('Bogota', 'Bogotá, D.C.'),
        ('Bolivar', 'Bolívar'),
        ('Boyaca', 'Boyacá'),
        ('Caldas', 'Caldas'),
        ('Caqueta', 'Caquetá'),
        ('Casanare', 'Casanare'),
        ('Cauca', 'Cauca'),
        ('Cesar', 'Cesar'),
        ('Choco', 'Chocó'),
        ('Cordoba', 'Córdoba'),
        ('Cundinamarca', 'Cundinamarca'),
        ('Guainia', 'Guainía'),
        ('Guaviare', 'Guaviare'),
        ('Huila', 'Huila'),
        ('La Guajira', 'La Guajira'),
        ('Magdalena', 'Magdalena'),
        ('Meta', 'Meta'),
        ('Narino', 'Nariño'),
        ('Norte de Santander', 'Norte de Santander'),
        ('Putumayo', 'Putumayo'),
        ('Quindio', 'Quindío'),
        ('Risaralda', 'Risaralda'),
        ('San Andres', 'San Andrés y Providencia'),
        ('Santander', 'Santander'),
        ('Sucre', 'Sucre'),
        ('Tolima', 'Tolima'),
        ('Valle del Cauca', 'Valle del Cauca'),
        ('Vaupes', 'Vaupés'),
        ('Vichada', 'Vichada'),
    ]

    # Generamos los años desde 2017 hasta el 2026 de forma dinámica
    ANOS_CHOICES = [(str(ano), str(ano)) for ano in range(2017, 2027)]

    municipio = models.CharField(max_length=100, verbose_name="Municipio")
    departamento = models.CharField(
        max_length=50, 
        choices=DEPARTAMENTOS_CHOICES, 
        verbose_name="Departamento"
    )
    ano = models.CharField(
        max_length=4,
        choices=ANOS_CHOICES,
        default='2017',
        verbose_name="Año del Mapa"
    )
    imagen_mapa = models.ImageField(upload_to='mapas_jpg/', verbose_name="Imagen del Mapa (JPG)")
    contexto_historico = models.TextField(blank=True, null=True, verbose_name="Análisis de Contexto / Memoria")
    coautores = models.CharField(max_length=200, default="Ivan CARROLL-JANER y Bognan Kadidja SEREME", verbose_name="Créditos de Autoría")
    fecha_registro = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Mapa de Líderes Sociales"
        verbose_name_plural = "Mapas de Líderes Sociales"
        ordering = ['-ano', 'departamento', 'municipio']

    def __str__(self):
        return f"[{self.ano}] {self.municipio} - {self.get_departamento_display()}"
