import email
from tabnanny import verbose
from django.db import models
from django.forms import CharField

# Create your models here.

class Pais(models.Model):
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
    pais = models.ForeignKey(Pais, on_delete=models.CASCADE)

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

    DESCUENTO_CHOICES = [
        ('20', '20'),
        ('25', '25'),
        ('30', '35'),
        ('35', '35'),
        ('40', '40'),
    ]

    SEXO_CHOICES = [
        ('M', 'M'),
        ('F', 'F'),
    ]

    num_dist = models.CharField(max_length=20, primary_key=True)
    nombre = models.CharField(max_length=200)
    descuento_choice = models.CharField(max_length=10, choices = DESCUENTO_CHOICES, default='20')
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)
    tel_casa = models.CharField(max_length=10)
    tel_cel = models.CharField(max_length=10)
    pais = models.CharField(max_length=100)
    estado = models.CharField(max_length=100)
    centro_alta = models.CharField(max_length=100)
    email = models.EmailField()
    fecha_ultima_compra = models.DateField()
    meses_sin_compra = models.IntegerField()
    fecha_alta = models.DateField()
    sexo = models.CharField(max_length=2, choices = SEXO_CHOICES, default = 'M')
    fecha_nacimiento = models.DateField()
    total_puntos = models.IntegerField()
    fecha_ultima_llamada = models.DateField()
    codigo_ultima_llamada = models.CharField(max_length=100)
    comentario = models.TextField()

    # campo ManyToMany
    campania = models.ManyToManyField(Campania)

    def __str__(self):
        return self.codigo_eo

    def display_campania(self):
        # nombre: campo de la tabla foranea que queremos mostrar
        # campania: atributo campania del modelo Contacto
        return ", ".join([i.nombre for i in self.campania.all()])


class RegistroExitoso(models.Model):

    EXITOSO_CHOICES = [
    ('Exitoso', 'Cambio de residencia ( permanente o temporal)'),
    ('Exitoso', 'Es para su consumo personal'),
    ('Exitoso', 'Falta de recursos economicos'),
    ('Exitoso', 'Falta de tiempo'),
    ('Exitoso', 'Informativa'),
    ('Exitoso', 'Motivos de salud'),
    ('Exitoso', 'No compra con su codigo'),
    ('Exitoso', 'No conoce formas de compra'),
    ('Exitoso', 'Otros'),
    ]

    razon = models.CharField(max_length=300, choices = EXITOSO_CHOICES, default = ' ')


class RegistroNoExitoso(models.Model):

    NO_EXITOSO_CHOICES = [
        ('No Exitoso', 'Linea fuera de servicio'),
        ('No Exitoso', 'No contesta'),
        ('No Exitoso', 'No le interesa se le brinde información'),
        ('No Exitoso', 'No se puede contactar por el horario'),
        ('No Exitoso', 'Numero del patrocinador'),
        ('No Exitoso', 'Telefono equivocado'),
    ]

    razon = models.CharField(max_length=300, choices = NO_EXITOSO_CHOICES, default = ' ')


class Resultado(models.Model):
    contacto = models.ForeignKey(Contacto, on_delete=models.CASCADE)
    registro_no_exi = models.ForeignKey(RegistroNoExitoso, on_delete=models.CASCADE)
    registro_exi = models.ForeignKey(RegistroExitoso, on_delete=models.CASCADE)
    remarcar = models.BooleanField()

# class RegistrosNoExitoso(models.Model):
#     descripcion = models.TextField()


# class RegistrosNoExitoso(models.Model):
#     descripcion = models.BooleanField(default=False)


