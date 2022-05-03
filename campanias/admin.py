
from django.contrib import admin
from pytz import HOUR
from .models import Cedi, Campania, Contacto

# ***************** REGISTROS NORMALES *******************
admin.site.register(Cedi)

# ***************** REGISTROS CON CLASE *******************
@admin.register(Campania)
class CampaniaAdmin(admin.ModelAdmin):    
    list_display = ('nombre', 'cedis','fecha_creacion', 'fecha_modificacion')
    list_filter = ('fecha_modificacion', )
    # fields = ['fecha_creacion', 'fecha_modificacion']
    readonly_fields = ('fecha_creacion', 'fecha_modificacion')
    search_fields = ['nombre', 'cedis']

admin.site.register(Contacto)