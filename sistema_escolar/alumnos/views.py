from sistema_escolar.crud import vistas_crud

from .models import Alumno

alumnos = vistas_crud(
    Alumno, 'alumnos', 'Alumnos',
    (('matricula', 'Matrícula'), ('nombre', 'Nombre'), ('apellidos', 'Apellidos'),
     ('correo', 'Correo'), ('carrera', 'Carrera')),
    campos=('matricula', 'nombre', 'apellidos', 'correo', 'carrera'),
)
