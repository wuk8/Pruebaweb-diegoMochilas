from django.db import models
from django.core.validators import RegexValidator

class comuna(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return str(self.nombre)

class contacto(models.Model):
    nombre = models.CharField(max_length=100)
    rut = models.CharField(max_length=10, validators=[RegexValidator(regex=r'^\d{9,10}$', message='El RUT debe tener entre 9 y 10 dígitos.')])
    telefono = models.CharField(max_length=15)
    direccion = models.CharField(max_length=255)
    comuna_choices = [
        ('Puente Alto', 'Puente Alto'),
        ('Pirque', 'Pirque'),
        ('La Pintana', 'La Pintana'),
        ('San Bernardo', 'San Bernardo'),
        ('La Florida', 'La Florida'),
    ]
    comuna = models.CharField(max_length=50, choices=comuna_choices)
    profesion = models.CharField(max_length=100)
    sexo = models.CharField(max_length=1, choices=[('M', 'Masculino'), ('F', 'Femenino')])
    ocupacion = models.CharField(max_length=100)
    puesto_empresa = models.CharField(max_length=100)

    def __str__(self):
        return str(self.nombre)

class Mochilas(models.Model):
    nombre_servicio = models.CharField(max_length=100)
    descripcion = models.TextField()
    costo = models.DecimalField(max_digits=10, decimal_places=2)
    duracion = models.CharField(max_length=50)
    requisitos = models.TextField()
    disponibilidad = models.CharField(max_length=100)

    def __str__(self):
        return str(self.nombre_servicio)

class ServicioManager(models.Manager):
    pass

class Servicio(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()

    objects = ServicioManager()  

    def __str__(self):
        return str(self.nombre)
