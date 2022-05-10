
from django.contrib import admin
from .models import Cedi, Campania, Contacto, Pais, Resultado


# ***************** REGISTROS NORMALES *******************
# admin.site.register(Estado)
#admin.site.register(Cedi)
# admin.site.register(Contacto)
admin.site.register(Resultado)

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

    # list_display = ('codigo_eo', 'nombres', 'apellido_paterno', 'descuento', 'display_campania')
    # search_fields = ['codigo_eo', 'descuento']
    # list_editable = ['display_campania']

    # Edición de nombre de columna de "display_cedis" a "Cedis"
    Contacto.display_campania.short_description = 'Campaña'
