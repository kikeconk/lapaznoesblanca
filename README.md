# LA PAZ NO ES BLANCA 🇨🇴🗺️
### Cartografía social y memoria territorial de líderes sociales asesinados en Colombia

**La Paz No Es Blanca®** es una plataforma web de cartografía social e investigación geoespacial dedicada a visibilizar, mapear y analizar de manera sistemática los patrones de violencia y asesinatos cometidos contra líderes y lideresas sociales en los municipios de Colombia. 

A través de la integración de análisis de datos socioantropológicos y herramientas de visualización espacial, el proyecto busca constituirse como una herramienta de memoria histórica, denuncia institucional y soporte técnico para procesos de paz e investigación académica en el territorio nacional.

---

## ⚖️ Aviso Legal y Propiedad Intelectual

> ⚠️ **IMPORTANTE:** **La Paz No Es Blanca** es una marca de la Fundación Poco a Poco registrada ante la **Superintendencia de Industria y Comercio (SIC)**
## de la República de Colombia. Queda prohibido cualquier uso comercial no autorizado, reproducción total o parcial del diseño de la marca,
## o usurpación de la identidad visual de la plataforma sin autorización expresa de su titular.
## Su uso en este repositorio es estrictamente con fines de desarrollo de software libre y consulta académica.

---

## 🚀 Arquitectura y Tecnologías Utilizadas

La plataforma está diseñada bajo una infraestructura escalable que combina el análisis espacial cuantitativo con la robustez del desarrollo web moderno:

*   **Backend:** [Django 6.0](https://www.djangoproject.com/) (Python 3.14) administrando la lógica relacional, modelos de datos dinámicos y la API de gestión territorial.
*   **Base de Datos:** SQLite (Entorno de desarrollo) / PostgreSQL (Producción) para el almacenamiento estructurado de coordenadas, variables sociopolíticas y descriptores municipales.
*   **Procesamiento Geospatial (Origen de Datos):** Procesamiento previo de coberturas de la Tierra y capas territoriales utilizando imágenes satelitales **Sentinel-2** a través de **QGIS**, **R Studio** y **Google Earth Engine (GEE)**.
*   **Infraestructura & Despliegue:** Alojado de forma continua en **Render** con enrutamiento personalizado de dominios y seguridad SSL automatizada.

---

## 📂 Estructura del Proyecto

El repositorio está organizado siguiendo la arquitectura limpia de aplicaciones de Django:

```text
├── db.sqlite3               # Base de datos local estructurada
├── manage.py                # Script de gestión de Django
├── requirements.txt         # Dependencias del entorno de Python
├── mapas/                   # Aplicación principal del ecosistema cartográfico
│   ├── migration/           # Historial de migraciones de base de datos
│   ├── models.py            # Modelos del mapa social (coordenadas, líderes, municipios)
│   ├── views.py             # Lógica de renderizado con capas de seguridad try-except
│   └── templates/           # Interfaces e index.html para visualización de mapas
└── web_lapaz/               # Configuración global del proyecto (settings, urls)
