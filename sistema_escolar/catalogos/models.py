from django.db import models

# Create your models here.
class Carrera(models.Model):
    # Atributos
    clave = models.CharField(max_length=10, unique=True)
    nombre = models.CharField(max_length=50)
    duracion = models.IntegerField(default=10)

    # Métodos
    def __str__(self):
        return self.nombre


class Plan(models.Model):
    clave = models.CharField(max_length=20)
    nombre = models.CharField(max_length=50)
    carrera = models.ForeignKey(Carrera, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = 'Planes de Estudio'
