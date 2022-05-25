

from django.views.defaults import page_not_found
from django.http import Http404
from django.shortcuts import redirect, render, get_object_or_404
from campanias.models import Campania, Cedi, Contacto, Pais, Resultado, RegistroExitoso, RegistroNoExitoso

# Create your views here.

# ##############################################
# VISTA ERROR 404
# ##############################################
def error_not_found(request, exception):
    return render(request, 'formulario/error_404.html')


# ##############################################
# VISTA INDEX
# ##############################################
def index(request):
    cedi = Cedi.objects.all()
    campania = Campania.objects.all()
    pais = Pais.objects.all()

    context = {
        'pais': pais,
        'cedi': cedi,
        'campania': campania,
    }
    return render(request, 'formulario/index.html', context=context)

# TODO: hacer select dependientes

# ##############################################
# VISTA FORMULARIO
# ##############################################
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
    # lista_contactos = get_object_or_404(campania=campania_select).filter(cedis=cedi_select)



    # devuelve los querysets de la lista_contactos que están en el campo contacto de tabla Resultado y 
    # sobre de ellos filtra los que están por remarcar 
    por_remarcar = Resultado.objects.filter(contacto__in =  lista_contactos).filter(remarcar = True)

    # devuelve los querysets de los contactos seleccionados que no están aún en la tabla Resultado
    remarcar_excluidos = lista_contactos.exclude(num_dist__in = Resultado.objects.values('contacto'))
    # print('excluido:', remarcar_excluidos)

    # si en la tabla Contactos hay contactos que aún no existen en la tabla Resultado, 
    # devuelve uno de ellos, sino, devuelve un contacto que está en la tabla resultado 
    # con el campo remarcar como True
    def contacto_pormarcar():  
        if remarcar_excluidos.count() > 0:
            return remarcar_excluidos[0]
        elif por_remarcar.count() > 0:
            return por_remarcar[0]
 

    contacto = contacto_pormarcar()
    # print(contacto)

    # si no existen registros para la consulta, levanta un 404:
    try:
        contacto = Contacto.objects.get(num_dist=contacto)
    except Contacto.DoesNotExist:
        raise Http404

    # Se obtienen los registros exitosos y no exitosos para poderlos 
    # elegir en el frontend
    registros_exitosos = RegistroExitoso.objects.all()
    registros_no_exitosos = RegistroNoExitoso.objects.all()

    # creación de contexto
    context = {
        'pais_select': pais_select,
        'cedi_select': cedi_select,
        'campania_select': campania_select,
        'descripcion_campania': descripcion_campania,
        'contacto': contacto,
        'registros_exitosos': registros_exitosos,
        'registros_no_exitosos': registros_no_exitosos,
    }
   
    return render(request, 'formulario/formulario.html', context=context)


# * El nombre del parámetro deberá ser igual en la vista y en la url, sino 
# * Desatará un error de submit_registro() got an unexpected keyword argument
def submit_registro(request, cedis, pais, campania):
    # print("cedi: ", cedis)
    # print("pais: ", pais)
    # print("campania: ", campania)


    check = request.POST.get('check_remarcar')
    # check_remarcar = request.POST['check_remarcar']
    print(check)

    context={
        'cedis':cedis,
        'pais': pais,
        'campania':campania,
    }
    return render(request, 'formulario/submit_registro.html', context=context)




def formulario2(request, pais, cedis, campania):
    pais_select = pais
    cedi_select = cedis
    campania_select = campania



    # QUERYSET: filtra las campañas por el nombre seleccionado y muestra su campo descripcion
    descripcion_campania = Campania.objects.get(nombre=campania_select) # .values('descripcion')   
    #print(descripcion_campania)


    # obtiene los querysets de los contactos que son de la campaña y cedis seleccionado
    lista_contactos = Contacto.objects.filter(campania=campania_select).filter(cedis=cedi_select)
    # lista_contactos = get_object_or_404(campania=campania_select).filter(cedis=cedi_select)



    # devuelve los querysets de la lista_contactos que están en el campo contacto de tabla Resultado y 
    # sobre de ellos filtra los que están por remarcar 
    por_remarcar = Resultado.objects.filter(contacto__in =  lista_contactos).filter(remarcar = True)

    # devuelve los querysets de los contactos seleccionados que no están aún en la tabla Resultado
    remarcar_excluidos = lista_contactos.exclude(num_dist__in = Resultado.objects.values('contacto'))
    # print('excluido:', remarcar_excluidos)

    # si en la tabla Contactos hay contactos que aún no existen en la tabla Resultado, 
    # devuelve uno de ellos, sino, devuelve un contacto que está en la tabla resultado 
    # con el campo remarcar como True
    def contacto_pormarcar():  
        if remarcar_excluidos.count() > 0:
            return remarcar_excluidos[0]
        elif por_remarcar.count() > 0:
            return por_remarcar[0]
 

    contacto = contacto_pormarcar()
    # print(contacto)

    # si no existen registros para la consulta, levanta un 404:
    try:
        contacto = Contacto.objects.get(num_dist=contacto)
    except Contacto.DoesNotExist:
        raise Http404

    # Se obtienen los registros exitosos y no exitosos para poderlos 
    # elegir en el frontend
    registros_exitosos = RegistroExitoso.objects.all()
    registros_no_exitosos = RegistroNoExitoso.objects.all()


    context={
        'pais_select': pais_select,
        'cedi_select': cedi_select,
        'campania_select': campania_select, 
        'descripcion_campania': descripcion_campania,
        'contacto': contacto,
        'registros_exitosos': registros_exitosos,
        'registros_no_exitosos': registros_no_exitosos,   
    }
    return render(request, 'formulario/formulario2.html', context=context)



# ######################################################
# VISTA DE FORMULARIO 
# ######################################################
# from .forms import ContactoForm

# EJEMPLO: 
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
