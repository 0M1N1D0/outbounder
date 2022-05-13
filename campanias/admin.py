
from tabnanny import verbose
from django.contrib import admin
from .models import Cedi, Campania, Contacto, Pais, Resultado, RegistroExitoso, RegistroNoExitoso


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


@admin.register(Contacto)
class ContactoAdmin(admin.ModelAdmin):
    pass
    # list_display = ('codigo_eo', 'nombres', 'apellido_paterno', 'descuento', 'display_campania')
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
    # Edición de nombre de columna de "display_cedis" a "Cedis"
    