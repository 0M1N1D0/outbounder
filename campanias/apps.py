from tabnanny import verbose
from django.apps import AppConfig


class CampaniasConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'campanias'

    verbose_name = 'Gestión de campañas'

    ordering = ['Pais', 'Cedi', 'Campania', 'RegistroExitoso', 'RegistroNoExitoso', 'Contacto', 'Resultado']