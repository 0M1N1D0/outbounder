
# from django import forms
# from campanias.models import Contacto

# class ContactoForm(forms.ModelForm):
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
    # class Meta:
    #     model = Contacto
    #     fields = ['nombre', 'campania']

    #     # creando las clases de HTML para acceder con Bootstrap 
    #     widgets = { 
    #         'nombre': forms.TextInput(attrs={'class': 'form-control'}),
    #         'campania': forms.SelectMultiple(attrs={'class': 'form-control'}),
    #     }

