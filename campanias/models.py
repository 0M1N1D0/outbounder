from pyexpat import model
from django.db import models

# Create your models here.

class Pais(models.Model):
    nombre = models.CharField(max_length=200, primary_key=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'País'
        verbose_name_plural = 'Países'


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
    descripcion = models.TextField()
    # campo manytomany
    cedis = models.ManyToManyField(Cedi)

    def __str__(self):
        return self.nombre 

    # método para list_display del campo cedis(ManyToMany)
    def display_cedis(self):
        # nombre: campo de la tabla foranea que queremos mostrar
        # cedis: atributo cedis del modelo Campania
        return ", ".join([i.nombre for i in self.cedis.all()])

    class Meta:
        verbose_name = 'Campaña'
        verbose_name_plural = 'Campañas'


class Contacto(models.Model):

    DESCUENTO_CHOICES = [
        ('20', '20'),
        ('25', '25'),
        ('30', '30'),
        ('35', '35'),
        ('40', '40'),
    ]

    SEXO_CHOICES = [
        ('M', 'M'),
        ('F', 'F'),
    ]

    num_dist = models.CharField(verbose_name='Número de distribuidor', max_length=20, primary_key=True, unique=False)
    nombre = models.CharField(max_length=200)
    descuento_choice = models.CharField(max_length=10, choices = DESCUENTO_CHOICES, default='20')
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    #fecha_modificacion = models.DateTimeField(auto_now=True)
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
    campania = models.ForeignKey(Campania, verbose_name='campaña', on_delete=models.CASCADE)

    def __str__(self):
        return self.num_dist


# EXITOSO_CHOICES = [
#     ('Exitoso', 'Cambio de residencia ( permanente o temporal)'),
#     ('Exitoso', 'Es para su consumo personal'),
#     ('Exitoso', 'Falta de recursos economicos'),
#     ('Exitoso', 'Falta de tiempo'),
#     ('Exitoso', 'Informativa'),
#     ('Exitoso', 'Motivos de salud'),
#     ('Exitoso', 'No compra con su codigo'),
#     ('Exitoso', 'No conoce formas de compra'),
#     ('Exitoso', 'Otros'),
# ]


class RegistroExitoso(models.Model):
    razon = models.CharField(max_length=300)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.razon

    class Meta:
        verbose_name = 'Registro Exitoso'
        verbose_name_plural = 'Registros Exitosos'


# NO_EXITOSO_CHOICES = [
#     ('No Exitoso', 'Linea fuera de servicio'),
#     ('No Exitoso', 'No contesta'),
#     ('No Exitoso', 'No le interesa se le brinde información'),
#     ('No Exitoso', 'No se puede contactar por el horario'),
#     ('No Exitoso', 'Numero del patrocinador'),
#     ('No Exitoso', 'Telefono equivocado'),
# ]

class RegistroNoExitoso(models.Model):
    razon = models.CharField(max_length=300)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.razon

    class Meta:
        verbose_name = 'Registro No Exitoso'
        verbose_name_plural = 'Registros No Exitosos'


class Resultado(models.Model):

    contacto = models.ForeignKey(Contacto, on_delete=models.CASCADE)
    registro_no_exi = models.ForeignKey(RegistroNoExitoso, on_delete=models.CASCADE, null=True, blank=True)
    registro_exi = models.ForeignKey(RegistroExitoso, on_delete=models.CASCADE, null=True, blank=True)
    comentario = models.TextField()
    remarcar = models.BooleanField()
    fecha_creacion = models.DateField(auto_now_add=True) 
    ultima_interaccion = models.DateTimeField(auto_now=True)
    
   # campania = Contacto.objects.all().select_related('campania')

    def __str__(self):
        # se transforma a str() porque si no devuelve un error 
        return str(self.contacto)
        


class Backup(models.Model):
    num_dist = models.CharField(max_length=20)
    nombres = models.CharField(max_length=200)
    descuento_choice = models.CharField(max_length=10)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    tel_casa = models.CharField(max_length=10)
    tel_cel = models.CharField(max_length=10)
    pais = models.CharField(max_length=100)
    estado = models.CharField(max_length=100)
    centro_alta = models.CharField(max_length=100)
    email = models.EmailField()
    fecha_ultima_compra = models.DateField()
    meses_sin_compra = models.IntegerField()
    fecha_alta = models.DateField()
    sexo = models.CharField(max_length=2)
    fecha_nacimiento = models.DateField()
    total_puntos = models.IntegerField()
    campania = models.CharField(max_length=200)
    pais = models.CharField(max_length=200)
    cedi = models.CharField(max_length=200)
    registro_no_exi = models.CharField(max_length=200)
    registro_exi = models.CharField(max_length=200)
    comentario = models.TextField()
    remarcar = models.BooleanField()
    ultima_interaccion = models.DateTimeField(auto_now=True)
    
    

"""
MéTODO PARA USAR UN CAMPO de una tabla many to many en list_display

def display_campania(self):
        # nombre: campo de la tabla foranea que queremos mostrar
        # campania: atributo campania del modelo Resultado
        return ", ".join([i.nombre for i in self.campania.all()])
"""
    

# class RegistrosNoExitoso(models.Model):
#     descripcion = models.TextField()


# class RegistrosNoExitoso(models.Model):
#     descripcion = models.BooleanField(default=False)


