from tabnanny import verbose
from django.db import models

# Create your models here.

class Estado(models.Model):
    nombre = models.CharField(max_length=200, primary_key=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre


class Cedi(models.Model):
    nombre = models.CharField(max_length=200, primary_key=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)
    # campo ForeignKey
    estado = models.ForeignKey(Estado, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre


class Campania(models.Model):
    nombre = models.CharField(max_length=200, primary_key=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)
    # campo manytomany
    cedis = models.ManyToManyField(Cedi)

    def __str__(self):
        return self.nombre 

    # método para list_display del campo cedis(ManyToMany)
    def display_cedis(self):
        # nombre: campo de la tabla foranea que queremos mostrar
        # cedis: atributo cedis del modelo Campania
        return ", ".join([i.nombre for i in self.cedis.all()])



class Contacto(models.Model):
    codigo_eo = models.CharField(max_length=20, primary_key=True)
    nombres = models.CharField(max_length=200)
    apellido_paterno = models.CharField(max_length=200)
    apellido_materno = models.CharField(max_length=200)
    descuento = models.SmallIntegerField(null=True, blank=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)
    telefono = models.BigIntegerField()
    # campo ManyToMany
    campania = models.ManyToManyField(Campania)

    def __str__(self):
        return self.codigo_eo

    def display_campania(self):
        # nombre: campo de la tabla foranea que queremos mostrar
        # campania: atributo campania del modelo Contacto
        return ", ".join([i.nombre for i in self.campania.all()])


# class RegistrosNoExitoso(models.Model):
#     descripcion = models.TextField()


# class RegistrosNoExitoso(models.Model):
#     descripcion = models.BooleanField(default=False)


