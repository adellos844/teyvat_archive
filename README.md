# ¿Que es Teyvat archive?

Teyvat archive es una plataforma web informativa diseñada para facilitar la gestión de datos y recursos sobre el videojuego Genshin Impact. El sistema funciona como una base de datos interactiva donde los usuarios pueden consultar fichas técnicas detalladas de los personajes, clasificándolos según su región, elemento y rareza, además de acceder a guías de equipamiento óptimo (builds) que sugieren las mejores combinaciones de armas y artefactos para cada rol de combate.

## Características

- **Catálogo Completo:** Consulta detallada de personajes filtrados por región, elemento y rareza.
- **Optimización de Equipamiento:** Glosario interactivo de builds recomendadas (armas, artefactos y roles de equipo como DPS, Sub-DPS o Support).
- **Panel de Control:** Administración total de la wiki mediante Django Admin para moderación de contenido.
- **Entorno Moderno:** Configuración local contenedorizada al 100% con Docker y Docker Compose sobre PostgreSQL.
- **Despliegue Continuo (CD):** Integración total con GitHub y la plataforma Render para producción.

## Stack Tecnológico

El núcleo del proyecto ha sido seleccionado minuciosamente para garantizar robustez, portabilidad y un rendimiento óptimo bajo estándares modernos de desarrollo web:

### Backend
- **Django 6.0.3:** Framework web de alto nivel basado en Python, utilizado bajo el patrón arquitectónico MVT (Model-View-Template).
- **Python 3.12+:** Lenguaje de programación robusto y eficiente en el procesamiento de datos.
- **PostgreSQL (15-Alpine):** Motor de base de datos relacional potente y escalable, utilizado tanto en la infraestructura local como en producción.
- **Pillow:** Procesamiento y optimización de imágenes para las fichas técnicas de los personajes.

### Frontend
- **HTML5:** Estructuración limpia y accesible de las vistas de la wiki.
- **CSS3:** Estilos a medida, transiciones y maquetación adaptativa.
- **JavaScript:** Programación del lado del cliente para gestionar la interactividad del buscador, el comportamiento de los filtros dinámicos y la carga de datos.

### Infraestructura y DevOps
- **Docker & Docker Compose:** Contenedorización del entorno completo para aislar la aplicación y la base de datos de forma idéntica al entorno real.
- **Render:** Plataforma PaaS (Platform as a Service) para el alojamiento cloud de la web y la base de datos productiva.
- **WhiteNoise 6.6.0:** Servicio encargado del almacenamiento, compresión eficiente y servido de archivos estáticos (CSS y JS) directamente en producción.
- **Gunicorn:** Servidor de aplicaciones WSGI para la ejecución del entorno multi-hilo en la nube.

## Instalación y Despliegue Local

### Opción A: Con Docker
Para levantar el entorno completo con la aplicación web y la base de datos PostgreSQL local de forma automática:

1. **Construir y arrancar los contenedores:**
   ```bash
   docker compose up --build
   docker compose exec web python manage.py migrate
   
Accedemos a la aplicación a través de: http://localhost:8000/

### Opción B: Sin Docker
python -m venv .venv

# En Windows:
.venv\Scripts\activate

# En macOS/Linux:
source .venv/bin/activate

pip install -r requirements.txt
python manage.py migrate
python manage.py runserver

Accedemos a la aplicación a través de: http://127.0.0.1:8000/

---

### Estructura del Repositorio
<pre>
teyvat_archive/
├── core/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── media/
│   ├── armas/
│   ├── banners/
│   └── personajes/
│       ├── disenos/
│       └── icons/
├── static/core/
│   ├── css/
│   └── js/
├── templates/
│   ├── core/
│   │   └── base.html
│   ├── registration/
│   │   ├── login.html
│   │   └── register.html
│   └── wiki/
│       ├── detalle_equipo.html
│       ├── detalle_personaje.html
│       ├── home.html
│       ├── lista_armas.html
│       ├── lista_equipos.html
│       ├── lista_personajes.html
│       └── perfil_usuario.html
├── wiki/
│   ├── migrations/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   ├── utils.py
│   └── views.py
├── .dockerignore
├── crear_admin.py
├── db.sqlite3
├── docker-compose.yml
├── Dockerfile
├── manage.py
├── README.md
├── requirements.txt
└── superuser.txt
</pre>

---

## ☁️ Configuración y Variables de Entorno (Producción en Render)

La arquitectura de producción está alojada en **Render** (PaaS), garantizando un pipeline de Integración y Despliegue Continuo (CI/CD) vinculado directamente a la rama principal de GitHub.

### Variables de Entorno Requeridas en la Nube

Para salvaguardar la integridad de la plataforma, se configuraron las siguientes claves en el panel de control de Render:

- `DEBUG`: `False` (Desactiva el modo depuración para evitar fugas de información).
- `SECRET_KEY`: Cadena criptográfica única para la firma de sesiones de usuario.
- `DATABASE_URL`: URI de conexión cifrada proporcionada por la base de datos PostgreSQL de Render.
- `PYTHON_VERSION`: `3.12.0` (Asegura que el contenedor cloud compile con la misma versión del entorno local).

### Pipeline de Despliegue Continuo (Render CD)
El despliegue en la nube se automatiza con cada `git push origin main` siguiendo este proceso:
1. **Build Command:** El servidor prepara el entorno e instala dependencias:
   ```bash
   pip install -r requirements.txt && python manage.py collectstatic --no-input && python manage.py migrate