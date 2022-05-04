
from django import forms
from apps.campanias.models import Contacto

class ContactoForm(forms.ModelForm):
    # ****************************************************
    # EJEMPLO CON LA CLASE FORM
    # ****************************************************
    # nombres = forms.CharField(max_length=200)
    # apellido_paterno = forms (max_length=200)
    # apellido_materno = forms.CharField(max_length=200)
    # descuento = forms.SmallIntegerField(null=True, blank=True)
    # telefono = forms.SmallIntegerField(null=True)


    # ****************************************************
    # EJEMPLO CON LA CLASE MODELFORM
    # ****************************************************
    class Meta:
        model = Contacto
        fields = ['nombres', 'apellido_paterno', 'apellido_materno', 'descuento', 'telefono', 'campania']

        # creando las clases de HTML para acceder con Bootstrap 
        widgets = { 
            'nombres': forms.TextInput(attrs={'class': 'form-control'}),
            'apellido_paterno': forms.TextInput(attrs={'class': 'form-control'}),
            'apellido_materno': forms.TextInput(attrs={'class': 'form-control'}),
            'descuento': forms.NumberInput(attrs={'class': 'form-control'}),
            'telefono': forms.NumberInput(attrs={'class': 'form-control'}),
            'campania': forms.Select(attrs={'class': 'form-control'}),
        }

