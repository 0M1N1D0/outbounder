from dataclasses import fields
from pyexpat import model
from django.contrib import admin
from .models import Cedi, Campania, Contacto, Pais, Resultado, RegistroExitoso, RegistroNoExitoso, Backup
from import_export.admin import ExportActionMixin, ImportMixin, ImportExportModelAdmin, ImportExportMixin, ExportMixin
from import_export import resources # para exportar a excel desde el admin site

# ***************** REGISTROS NORMALES *******************
# admin.site.register(Estado)
admin.site.register(RegistroNoExitoso)
admin.site.register(RegistroExitoso)
#admin.site.register(Resultado)

# ***************** REGISTROS CON CLASE *******************

@admin.register(Campania)
class CampaniaAdmin(admin.ModelAdmin):    
    list_display = ('nombre', 'display_cedis')
    list_filter = ('nombre',)
    # fields = ['fecha_creacion', 'fecha_modificacion']
    readonly_fields = ('fecha_creacion', 'fecha_modificacion')
    search_fields = ['nombre', 'cedis']

    # Edición de nombre de columna de "display_cedis" a "Cedis"
    Campania.display_cedis.short_description = "Cedis"



@admin.register(Pais)
class PaisAdmin(admin.ModelAdmin): 
    list_display = ('nombre',)
    readonly_fields = ('fecha_creacion', 'fecha_modificacion')
    ordering = ('nombre',)


@admin.register(Cedi)
class CediAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'pais')
    ordering = ('nombre',)


# para agregar el boton importar primero se le 
# agrega la clase Resource y se especifica el 
# id como num_dist con la opción import_id_fields, 
# sino daría un error de id
class ContactoResource(resources.ModelResource):
    class Meta:
        model = Contacto
        import_id_fields = ('num_dist',)


'''
IMPORTANTE: el archivo contactos.csv, en las columnas de fecha, 
ponerlas en formato: mm/dd/aaaa
'''

# se agrega ImportMixin para agregar el boton Importar
# y se relaciona la clase resource
@admin.register(Contacto)
class ContactoAdmin(ImportMixin, admin.ModelAdmin):

    resource_class = ContactoResource

    # metodo para mostrar la FK campania
    def mostrar_campania(self, obj):
        if obj.campania:
            return obj.campania.nombre

    list_display = ('num_dist', 'mostrar_campania', 'fecha_creacion')
    # search_fields = ['codigo_eo', 'descuento']
    # list_editable = ['display_campania']



@admin.register(Resultado)
class ResultadoAdmin(admin.ModelAdmin):

    # método para mostrar en list_display un campo de tabla foránea 
    def mostrar_campania(self, obj):
        if obj.contacto:
            return obj.contacto.campania

    list_display = ('contacto', 'remarcar', 'ultima_interaccion', 'mostrar_campania')
    list_filter = ('contacto__campania', 'remarcar')
    search_fields = ['contacto__num_dist',]
    # readonly_fields = [] 
"""
mandar llamar al list_display un campo de una tabla con relacion manytomany
Resultado.display_campania.short_description = 'Campaña'
"""

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
    )
admin.site.register(Backup, BackupAdmin)
    