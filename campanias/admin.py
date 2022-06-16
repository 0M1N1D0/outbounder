from django.contrib import admin
from .models import Cedi, Campania, Contacto, Pais, Resultado, RegistroExitoso, RegistroNoExitoso, Backup
from import_export.admin import ImportExportMixin, ExportMixin
from import_export import resources # para exportar a excel desde el admin site

# ***************** REGISTROS NORMALES *******************
# admin.site.register(Estado)
admin.site.register(RegistroNoExitoso)
admin.site.register(RegistroExitoso)
#admin.site.register(Resultado)

# ***************** REGISTROS CON CLASE *******************

'''
IMPORTANTE: para la importación, los archivos .csv en las columnas de fecha 
ponerlas en formato: mm/dd/aaaa. 

IMPORTANTE: el nombre de las columnas en los archivos .csv debe ser igual 
al nombre del campo de la tabla de la base de datos.

IMPORTANTE: para agregar el boton importar primero se le 
agrega la clase Resource y se especifica el 
id con la opción import_id_fields, 
sino daría un error de id
'''

# *************************************************************
# CampaniaResource
# *************************************************************
class CampaniaResource(resources.ModelResource):
    class Meta:
        model = Campania
        import_id_fields = ('nombre',)
        fields = ('nombre', 'descripcion', 'fecha_creacion')


# *************************************************************
# CampaniaAdmin
# *************************************************************
@admin.register(Campania)
class CampaniaAdmin(ImportExportMixin, admin.ModelAdmin):   
    # conecta con CampaniaResource
    resource_class = CampaniaResource 
    list_display = ('nombre', 'display_cedis')
    list_filter = ('nombre',)
    # fields = ['fecha_creacion', 'fecha_modificacion']
    readonly_fields = ('fecha_creacion', 'fecha_modificacion')
    search_fields = ['nombre', 'cedis']

    # Edición de nombre de columna de "display_cedis" a "Cedis"
    Campania.display_cedis.short_description = "Cedis"


# *************************************************************
# PaisResource
# *************************************************************
class PaisResource(resources.ModelResource):
    class Meta:
        model = Pais
        import_id_fields = ('nombre',)
        fields = ('nombre',)


# *************************************************************
# PaisAdmin
# *************************************************************
@admin.register(Pais)
class PaisAdmin(ImportExportMixin, admin.ModelAdmin): 
    resource_class = PaisResource
    list_display = ('nombre',)
    readonly_fields = ('fecha_creacion', 'fecha_modificacion')
    ordering = ('nombre',)


# *************************************************************
# CediResource
# *************************************************************
class CediResource(resources.ModelResource):
    class Meta:
        model = Cedi
        import_id_fields = ('nombre',)
        fields = ('nombre', 'pais')


# *************************************************************
# CediAdmin
# *************************************************************
@admin.register(Cedi)
class CediAdmin(ImportExportMixin, admin.ModelAdmin):
    resource_class = CediResource
    list_display = ('nombre', 'pais')
    ordering = ('nombre',)


# *************************************************************
# ContactoResource
# *************************************************************
class ContactoResource(resources.ModelResource):
    class Meta:
        model = Contacto
        import_id_fields = ('num_dist',)
        fields = (
            'num_dist',
            'nombre',
            'descuento_choice',
            'fecha_creacion',
            'tel_casa',
            'tel_cel',
            'pais',
            'estado',
            'centro_alta',
            'email',
            'fecha_ultima_compra',
            'meses_sin_compra',
            'fecha_alta',
            'sexo',
            'fecha_nacimiento',
            'total_puntos',
            'campania',
            'cedis'
        )


# *************************************************************
# ContactoAdmin
# *************************************************************
# se agrega ImportMixin para agregar el boton Importar
# y se relaciona la clase resource
@admin.register(Contacto)
class ContactoAdmin(ImportExportMixin, admin.ModelAdmin):

    resource_class = ContactoResource

    # metodo para mostrar la FK campania
    def campania(self, obj):
        if obj.campania:
            return obj.campania.nombre

    # metodo para mostrar la FK cedis
    def cedis(self, obj):
        if obj.cedis:
            return obj.cedis.nombre

    list_display = ('num_dist', 'nombre', 'campania', 'cedis', 'tel_casa', 'tel_cel')
    list_filter = ('cedis', 'campania')
    readonly_fields = ('fecha_creacion',)
    search_fields = ['num_dist', 'nombre', 'campania__nombre', 'cedis__nombre']
    # list_editable = ['display_campania']


# *************************************************************
# ResultadoResource
# *************************************************************
class ResultadoResource(resources.ModelResource):
    class Meta:
        model = Resultado
        import_id_fields = ('contacto',)
        fields = (
            'contacto', 
            'registro_no_exi', 
            'registro_exi', 
            'comentario', 
            'remarcar', 
            'fecha_primer_contacto', 
            'ultima_interaccion'
        )


# *************************************************************
# ResultadoAdmin
# *************************************************************
@admin.register(Resultado)
class ResultadoAdmin(ExportMixin, admin.ModelAdmin):

    # método para mostrar en list_display un campo de tabla foránea 
    def mostrar_campania(self, obj):
        if obj.contacto:
            return obj.contacto.campania

    # método para mostrar en list_display un campo de tabla foránea 
    def mostrar_cedis(self, obj):
        if obj.contacto:
            return obj.contacto.cedis

    list_display = ('contacto', 'remarcar', 'ultima_interaccion', 'mostrar_campania', 'mostrar_cedis')
    list_filter = ('contacto__campania', 'remarcar')
    search_fields = ['contacto__num_dist',]
    # readonly_fields = [] 
"""
mandar llamar al list_display un campo de una tabla con relacion manytomany
Resultado.display_campania.short_description = 'Campaña'
"""


# *************************************************************
# BackupAdmin
# *************************************************************
# Se le agrega el botón exportar con ExportMixin
class BackupAdmin(ExportMixin, admin.ModelAdmin):
    list_display = (
        'num_dist',
        'nombres',
        'tel_casa',
        'tel_cel',
        'campania',
        'cedi',
        'registro_no_exi',
        'registro_exi',
        'remarcar',
        'fecha_interaccion',
    )
admin.site.register(Backup, BackupAdmin)
    