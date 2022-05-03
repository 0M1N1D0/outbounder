
from django.db import models

# Create your models here.

class Cedi(models.Model):
    nombre = models.CharField(max_length=200)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre


class Campania(models.Model):
    nombre = models.CharField(max_length=200)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)
    cedis = models.ForeignKey(Cedi, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre 


class Contacto(models.Model):
    nombres = models.CharField(max_length=200)
    apellido_paterno = models.CharField(max_length=200)
    apellido_materno = models.CharField(max_length=200)
    descuento = models.SmallIntegerField(null=True, blank=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)
    telefono = models.SmallIntegerField(null=True)
    
    campania = models.ManyToManyField(Campania)

    def __str__(self):
        return self.nombres


# class RegistrosNoExitoso(models.Model):
#     descripcion = models.TextField()


# class RegistrosNoExitoso(models.Model):
#     descripcion = models.BooleanField(default=False)


