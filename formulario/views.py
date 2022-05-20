

from logging import exception
from django.http import Http404
from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse   
from campanias.models import Campania, Cedi, Contacto, Pais, Resultado

# Create your views here.

def error_not_found(request, exception):
    return render(request, 'formulario/error_404.html', status=404)


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

    # try:
    # obtiene los querysets de los contactos que son de la campaña y cedis seleccionado
    lista_contactos = Contacto.objects.filter(campania=campania_select).filter(cedis=cedi_select)
    #lista_contactos = get_object_or_404(campania=campania_select).filter(cedis=cedi_select)
    # except Contacto.DoesNotExist:
    #     raise Http404


    # devuelve los querysets de la lista_contactos que están en el campo contacto de tabla Resultado y 
    # sobre de ellos filtra los que están por remarcar 
    por_remarcar = Resultado.objects.filter(contacto__in =  lista_contactos).filter(remarcar = True)

    # devuelve los querysets de los contactos seleccionados que no están aún en la tabla Resultado
    remarcar_excluidos = lista_contactos.exclude(num_dist__in = Resultado.objects.values('contacto'))
    print('excluido:', remarcar_excluidos)

    # si en la tabla Contactos hay contactos que aún no existen en la tabla Resultado, 
    # devuelve uno de ellos, sino, devuelve un contacto que está en la tabla resultado 
    # con el campo remarcar como True
    def contacto_pormarcar():  
        if remarcar_excluidos.count() > 0:
            return remarcar_excluidos[0]
        elif por_remarcar.count() > 0:
            return por_remarcar[0]
 

    contacto = contacto_pormarcar()
    print(contacto)

    # si no existen registros para la consulta, levanta un 404:
    try:
        consulta = Contacto.objects.get(num_dist=contacto)
        print(consulta)
    except Contacto.DoesNotExist:
        raise Http404


    context = {
        'pais_select': pais_select,
        'cedi_select': cedi_select,
        'campania_select': campania_select,
        'descripcion_campania': descripcion_campania,
        'contacto': consulta,
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
