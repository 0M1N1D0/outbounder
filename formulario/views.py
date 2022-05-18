
from multiprocessing import context
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse   
from campanias.models import Campania, Cedi, Contacto, Pais, Resultado

# Create your views here.

# **********************************************
# VISTA INDEX
# **********************************************
def index(request):
    cedi = Cedi.objects.all()
    campania = Campania.objects.all()
    pais = Pais.objects.all()
    #campanias = Campania.objects.filter(cedis = cedi[0])
    # campanias = Campania.objects.select_related('cedis').filter(cedis=cedi)
    context = {
        'pais': pais,
        'cedi': cedi,
        'campania': campania,
    }
    return render(request, 'formulario/index.html', context=context)

# TODO: hacer select dependientes

# **********************************************
# VISTA FORMULARIO
# **********************************************
def formulario(request):
    # se guardan los datos seleccionados con <select>
    cedi_select  = request.POST['select_cedis']
    campania_select  = request.POST['select_campania']
    pais_select = request.POST['select_pais']

    # QUERYSET: filtra las campañas por el nombre seleccionado y muestra su campo descripcion
    descripcion_campania = Campania.objects.get(nombre=campania_select) # .values('descripcion')   
    #print(descripcion_campania)

    # obtiene los querysets de los contactos que son de la campaña y cedis seleccionado
    lista_contactos = Contacto.objects.filter(campania=campania_select).filter(cedis=cedi_select)
    #print(lista_contactos)

    # devuelve los querysets que la lista_contactos que están en el campo contacto y 
    # sobre de ellos filtra los que están por remarcar 
    por_remarcar = Resultado.objects.filter(contacto__in =  lista_contactos).filter(remarcar = True)
    #print(por_remarcar)

    def contacto_pormarcar():
        if por_remarcar.count() > 0:
            return por_remarcar[0]
        else:
            return None
 
    contacto = contacto_pormarcar()
    print(contacto)
    q = Contacto.objects.get(num_dist=contacto)
    print(q)
    context = {
        'pais_select': pais_select,
        'cedi_select': cedi_select,
        'campania_select': campania_select,
        'descripcion_campania': descripcion_campania,
        'contacto': q,
    }

    # lista_cedis = Cedi.objects.filter(pais=pais_select)    

    return render(request, 'formulario/formulario.html', context=context)


# ******************************************************
# VISTA DE FORMULARIO
# ******************************************************
# from .forms import ContactoForm

# def index(request):
#     context={}
#     if request.method == 'POST':
#         form = ContactoForm(request.POST or None, request.FILES or None)
#         if form.is_valid():
#             # process the data in form.cleaned_data as required
#             #nombres = form.cleaned_data['nombres']
#             # ...
#             # redirect to a new URL:
#             form.save()

#      # if a GET (or any other method) we'll create a blank form
#     else:
#         form = ContactoForm()
#     context['form'] = form
#     return render(request, 'formulario/index.html', context)