
from django.contrib import admin
from .models import Cedi, Campania, Contacto, Estado

# ***************** REGISTROS NORMALES *******************
# admin.site.register(Estado)
admin.site.register(Cedi)
admin.site.register(Contacto)
# admin.site.register(Estado)

# ***************** REGISTROS CON CLASE *******************
@admin.register(Campania)
class CampaniaAdmin(admin.ModelAdmin):    
    # list_display = ('nombre', 'cedis','fecha_creacion', 'fecha_modificacion')
    list_filter = ('fecha_modificacion', )
    # fields = ['fecha_creacion', 'fecha_modificacion']
    readonly_fields = ('fecha_creacion', 'fecha_modificacion')
    search_fields = ['nombre', 'cedis']



@admin.register(Estado)
class EstadoAdmin(admin.ModelAdmin): 
    list_display = ('nombre', 'fecha_creacion', 'fecha_modificacion')

