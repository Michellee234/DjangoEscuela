from django.db import models

# Create your models here.
from catalogos.models import Carrera


class Alumno(models.Model):
    matricula = models.CharField('matrícula', max_length=20, unique=True)
    nombre = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    correo = models.EmailField(blank=True)
    carrera = models.ForeignKey(Carrera, on_delete=models.PROTECT)

    def __str__(self):
        return f'{self.matricula} · {self.nombre} {self.apellidos}'
