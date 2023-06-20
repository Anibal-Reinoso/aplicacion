from django.db import models
import datetime

# Create your models here.
class Escuela(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.nombre

class Profesor(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    edad = models.IntegerField()
    email = models.EmailField(verbose_name="Mail del profesor", unique=True)
    celular = models.CharField(max_length=15, null=True)
    telefono = models.CharField(max_length=15, default="")
    egreso = models.IntegerField(default=2009)
    fecha_contratacion = models.DateField(datetime.date.today())

    def __str__(self):
        return self.apellido

class RegistroProfesorEscuela(models.Model):
    profesor = models.ForeignKey(Profesor, null=True, on_delete=models.SET_NULL)
    escuela = models.ForeignKey(Escuela, null=True, on_delete=models.SET_NULL)
    detalle = models.TextField(max_length=200, null=True)
    horas = models.IntegerField(null=True)
