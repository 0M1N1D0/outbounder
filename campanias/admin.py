from dataclasses import fields
from django.contrib import admin
from .models import Cedi, Campania

# ***************** REGISTROS NORMALES *******************
admin.site.register(Cedi)

# ***************** REGISTROS CON CLASE *******************
@admin.register(Campania)
class CampaniaAdmin(admin.ModelAdmin):    
    list_display = ('nombre', 'cedis')
    search_fields = ['nombre', 'cedis']