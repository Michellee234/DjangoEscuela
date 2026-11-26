# Sistema Escolar con Django

Aplicación web académica que centraliza el acceso a catálogos, inscripción, tutorías y usuarios. La versión actual usa PostgreSQL y permite consultar y registrar carreras desde el portal, así como administrar carreras y planes de estudio desde el panel de Django.

El alcance funcional se revisó en el [commit `7d1f559` del repositorio](https://github.com/Michellee234/DjangoEscuela/tree/7d1f559963fbdb505aca5b642d7380bbbeb16574). Ese commit y el ZIP de referencia usan SQLite. La configuración local actual del proyecto usa PostgreSQL.

## Alcance actual

| Módulo | Ruta | Estado de la versión revisada |
| --- | --- | --- |
| Inicio | `/` | Pantalla principal y menú de navegación. |
| Catálogos | `/catalogos/` | Menú de catálogos. La opción Carreras permite consultar y registrar carreras. Alumnos, Materias y Grupos aparecen como opciones informativas. |
| Inscripción | `/inscripcion/` | Menú con opciones para registrar, consultar, modificar y cancelar una inscripción. Los flujos están pendientes de implementación. |
| Tutorías | `/tutorias/` | Pantalla informativa del módulo. La gestión de tutorías está pendiente de implementación. |
| Usuarios | `/usuarios/` | Formulario visual con correo, nombre y teléfono. El guardado de usuarios desde este formulario está pendiente. |
| Alumnos | Sin ruta propia | App incluida en la configuración del proyecto, pendiente de modelos y pantallas. |
| Administración de Django | `/admin/` | Panel para administrar carreras y planes de estudio con una cuenta autorizada. |

## Instalación local

Usa **Python 3.12**, **Django 5.1.1**, un servidor de **PostgreSQL** en ejecución y el controlador **Psycopg**. Django 5.1 requiere [PostgreSQL 13 o superior](https://docs.djangoproject.com/en/5.1/ref/databases/#postgresql-notes). Si ya tienes una copia del proyecto, entra en la carpeta donde está `manage.py` y crea el entorno virtual. Para obtener una copia desde GitHub, usa Git.

```bash
git clone https://github.com/Michellee234/DjangoEscuela.git
cd DjangoEscuela/sistema_escolar
```

En macOS o Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

En Windows con PowerShell:

```powershell
py -3.12 -m venv .venv
.\.venv\Scripts\Activate.ps1
```

Instala las dependencias con el entorno activo:

```bash
python -m pip install "Django==5.1.1" "psycopg[binary]>=3.1.8,<4"
```

### Configurar PostgreSQL

1. Inicia el servidor de PostgreSQL. En macOS, puedes hacerlo con **Postgres.app**.
2. Crea o selecciona la base `gestion_escolar`. Usa un rol de PostgreSQL con permiso para conectarse y crear tablas en el esquema que utiliza Django. En un entorno local, puedes usar el rol propietario de la base.
3. Revisa `sistema_escolar/settings.py`. Si tu copia aún apunta a SQLite, reemplaza el bloque `DATABASES` con una configuración de PostgreSQL como la siguiente. Si ya tienes configurado PostgreSQL, usa los valores de tu instalación.

```python
import os

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.environ.get("DB_NAME", "gestion_escolar"),
        "USER": os.environ["DB_USER"],
        "PASSWORD": os.environ.get("DB_PASSWORD", ""),
        "HOST": os.environ.get("DB_HOST", "localhost"),
        "PORT": os.environ.get("DB_PORT", "5432"),
    }
}
```

Con este ejemplo, define `DB_USER` en la misma terminal antes de ejecutar Django (`export DB_USER=tu_usuario` en macOS o Linux, o `$env:DB_USER = 'tu_usuario'` en PowerShell). Define `DB_PASSWORD` si el servidor solicita contraseña y ajusta `DB_NAME`, `DB_HOST` y `DB_PORT` si tu instalación usa otros valores. Guarda las credenciales como variables de entorno.

### Aplicar migraciones y ejecutar el sistema

```bash
python manage.py migrate
python manage.py check
python manage.py runserver
```

Abre [http://127.0.0.1:8000/](http://127.0.0.1:8000/). `migrate` aplica la estructura de tablas en la base PostgreSQL que ya creaste. Si necesitas conservar registros de una base SQLite anterior, la transferencia de esos datos es un paso aparte.

Para ingresar al panel administrativo, crea una cuenta local con `python manage.py createsuperuser` desde otra terminal con el entorno activo y abre [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/).

## Registrar y consultar una carrera

1. En el menú lateral, selecciona **Catálogos** y después **Carreras**.
2. Haz clic en **Nueva Carrera**.
3. Captura la clave, el nombre y la duración. Para una demostración puedes usar `TIC01`, `Ingeniería en TIC` y `9` con una clave que todavía no exista en tu base.
4. Presiona **Guardar**. La aplicación regresa al catálogo y muestra el nuevo registro en la tabla.

La clave admite hasta 10 caracteres y debe ser única. Si intentas registrarla por segunda vez, el formulario muestra un error y conserva el registro original. Para modificar o eliminar una carrera en esta versión, utiliza el panel de administración.

## Estructura técnica

| Ubicación dentro de `sistema_escolar/` | Responsabilidad |
| --- | --- |
| `manage.py` | Comandos locales de Django, como migrar la base e iniciar el servidor. |
| `sistema_escolar/settings.py` y `sistema_escolar/urls.py` | Configuración de Django y distribución de rutas por app. |
| `catalogos/` | Modelos `Carrera` y `Plan`, formulario `CarreraForm`, vistas, rutas y migraciones. |
| `inicio/`, `inscripcion/`, `tutorias/`, `usuarios/` y `alumnos/` | Apps del portal escolar en distintos estados de implementación. |
| `templates/base.html` | Plantilla común de Django que integra la estructura de SB Admin. |
| `static/` | Recursos CSS y JavaScript de SB Admin, incluido Bootstrap 5.2.3. |

Django dirige cada solicitud a una vista según la URL. En el listado de carreras, la vista consulta el modelo `Carrera` mediante el ORM y entrega los registros a `catalogos/listarCarreras.html`. En el alta, `CarreraForm` valida los datos, el ORM guarda el registro en PostgreSQL y la vista redirige al listado.

### Plantilla y diseño de la interfaz

La interfaz del portal se diseñó a partir de **SB Admin 7.0.7**, una plantilla de panel administrativo de Start Bootstrap. Se adaptaron la barra superior, el menú lateral y el área de contenido para incorporar la navegación y las pantallas del Sistema Escolar. Los módulos que utilizan `base.html` comparten esta estructura y muestran su contenido mediante los bloques de plantillas de Django. Los estilos y scripts se cargan desde `static/` con la etiqueta `{% static %}`.

Crédito de la plantilla a [Start Bootstrap](https://startbootstrap.com/template/sb-admin), con [licencia MIT](https://github.com/StartBootstrap/startbootstrap-sb-admin/blob/v7.0.7/LICENSE).

### Modelo de datos

| Modelo | Tabla | Campos principales |
| --- | --- | --- |
| `Carrera` | `catalogos_carrera` | `id` (clave primaria), `clave` (texto, máximo 10, única), `nombre` (texto, máximo 50), `duracion` (entero, valor predeterminado 10). |
| `Plan` | `catalogos_plan` | `id` (clave primaria), `clave` (texto, máximo 20), `nombre` (texto, máximo 50), `carrera_id` (clave foránea obligatoria). |

Una carrera puede tener cero o varios planes de estudio. Cada plan pertenece a una carrera. La relación aplica eliminación en cascada cuando se elimina una carrera a través de Django.

## Pruebas y pendientes

Los resultados siguientes corresponden al commit `7d1f559`, verificado con una base SQLite nueva. Para incorporar evidencia de la versión con PostgreSQL, ejecuta nuevamente las comprobaciones de migraciones, registro y listado de carreras en `gestion_escolar`.

| Comprobación | Resultado observado |
| --- | --- |
| Configuración, migraciones y correspondencia entre modelos y migraciones | `check`, `migrate` y `makemigrations --check --dry-run` terminaron correctamente. |
| Inicio, Catálogos, Inscripción, Tutorías y Usuarios | Las cinco pantallas principales respondieron correctamente. |
| Consulta y alta de carreras | Se mostró el mensaje de catálogo vacío, se registró una carrera y el listado mostró la fila guardada. |
| Clave de carrera duplicada | El formulario mostró un error y la base conservó un solo registro. |
| Edición y eliminación de carreras desde el portal | Los botones del listado están sin conectar. Al abrir las pantallas por sus rutas, Django devolvió un error de plantilla. |
| Listados administrativos de carreras y planes | Ambos abrieron con una sesión administrativa. |

`python manage.py test` encontró cero pruebas definidas en los archivos del proyecto. Quedan pendientes la edición y eliminación desde el portal, la gestión de alumnos, materias y grupos, los flujos de inscripción y tutorías y el registro de usuarios desde su formulario.
