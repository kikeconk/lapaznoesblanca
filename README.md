# LA PAZ NO ES BLANCA 🇨🇴🗺️
### Cartografía social y memoria territorial de líderes sociales asesinados en Colombia

**La Paz No Es Blanca®** es una plataforma web de cartografía social e investigación geoespacial dedicada a visibilizar, mapear y analizar de manera sistemática los patrones de violencia y asesinatos cometidos contra líderes y lideresas sociales en los municipios de Colombia. 

A través de la integración de análisis de datos socioantropológicos y herramientas de visualización espacial, el proyecto busca constituirse como una herramienta de memoria histórica, denuncia institucional y soporte técnico para procesos de paz e investigación académica en el territorio nacional.

---

## ⚖️ Aviso Legal y Propiedad Intelectual

> ⚠️ **IMPORTANTE:** **La Paz No Es Blanca** es una marca de la Fundación Poco a Poco registrada ante la **Superintendencia de Industria y Comercio (SIC)** de la República de Colombia. Queda prohibido cualquier uso comercial no autorizado, reproducción total o parcial del diseño de la marca,
o usurpación de la identidad visual de la plataforma sin autorización expresa de su titular.
> Su uso en este repositorio es estrictamente con fines de desarrollo de software libre y consulta académica.


---

## 🚀 Arquitectura y Tecnologías Utilizadas

El ecosistema del proyecto está construido con herramientas robustas de código abierto y servicios en la nube para garantizar estabilidad y persistencia:

* **Backend:** Python 3.12 + Django Framework (v6.0.6)
* **Servidor de Producción (Web Host):** [Render](https://render.com/) (Entorno administrado bajo Python 3.12.3)
* **Base de Datos:** PostgreSQL / SQLite (Desarrollo local)
* **Almacenamiento en la Nube (Multimedia):** [Cloudinary](https://cloudinary.com/) (Garantiza que los archivos `.jpg` de los mapas sean permanentes y no se borren con los reinicios del servidor efímero).
* **Procesamiento de Imágenes:** Pillow (Librería nativa de Python para el manejo de `ImageField`).
* **Servidor WSGI:** Gunicorn

---

## 📦 Dependencias Core (`requirements.txt`)

Para asegurar despliegues limpios en entornos Cloud sin conflictos de paquetes locales (como los generados por entornos Anaconda), el proyecto utiliza estrictamente las siguientes dependencias esenciales:

```text
Django==6.0.6
cloudinary==1.45.0
django-cloudinary-storage
gunicorn==23.0.0
Pillow==10.3.0

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
└── lapaznoesblanca/               # Configuración global del proyecto (settings, urls)
