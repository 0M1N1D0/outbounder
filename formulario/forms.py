
from django import forms
from campanias.models import Contacto

class ContactoForm(forms.ModelForm):
    # nombres = forms.CharField(max_length=200)
    # apellido_paterno = forms (max_length=200)
    # apellido_materno = forms.CharField(max_length=200)
    # descuento = forms.SmallIntegerField(null=True, blank=True)
    # telefono = forms.SmallIntegerField(null=True)


    class Meta:
        model = Contacto
        fields = ['nombres', 'apellido_paterno', 'apellido_materno', 'descuento', 'telefono', 'campania']