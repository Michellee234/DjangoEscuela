from sistema_escolar.crud import rutas_crud

from .views import alumnos

urlpatterns = rutas_crud('alumnos', alumnos)