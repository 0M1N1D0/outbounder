from django.db import models

# Create your models here.

class Cedi(models.Model):
    nombre = models.CharField(max_length=200)
    fecha_creacion = models.DateField(auto_now_add=True)
    fecha_modificacion = models.DateField(auto_now=True)

    def __str__(self):
        return self.nombre


class Campania(models.Model):
    nombre = models.CharField(max_length=200)
    fecha_creacion = models.DateField(auto_now_add=True)
    fecha_modificacion = models.DateField(auto_now=True)
    cedis = models.ForeignKey(Cedi, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre 