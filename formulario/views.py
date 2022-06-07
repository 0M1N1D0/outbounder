

from django.http import Http404
from django.shortcuts import render
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

    context = consulta(pais_select, cedi_select, campania_select)
   
    return render(request, 'formulario/formulario.html', context=context)

# ##############################################
# VISTA SUBMIT REGISTRO
# ##############################################
# * El nombre del parámetro deberá ser igual en la vista y en la url, sino 
# * desatará un error de submit_registro() got an unexpected keyword argument
def submit_registro(request, cedis, pais, campania, num_dist):

    # * de esta forma no es posible porque da error al no marcar el check
    # * check = request.POST['check_remarcar']

    # obtención de datos
    check = request.POST.get('check_remarcar')
    registro_exitoso = request.POST['registro_exitoso']
    registro_no_exitoso = request.POST['registro_no_exitoso']
    textarea = request.POST['textarea']


    print(check)
    print(registro_exitoso)
    print(num_dist)
    print(registro_no_exitoso)
    print(textarea)

    '''
    Primero se obtienen las instancias con las opciones, 
    y estas se ponen en la creación del registro, ya que si 
    se ponen las opciones en directo, da error. 
    '''
    contacto = Contacto.objects.get(num_dist=num_dist)
    reg_exi = RegistroExitoso.objects.get(razon=registro_exitoso)
    reg_no_exi = RegistroNoExitoso.objects.get(razon=registro_no_exitoso)

    registro = Resultado(contacto=contacto, registro_no_exi=reg_no_exi, registro_exi=reg_exi, comentario=textarea, remarcar=check)
    registro.save()

    context={
        'cedis':cedis,
        'pais': pais,
        'campania':campania,
    }
    return render(request, 'formulario/submit_registro.html', context=context)



# ##############################################
# VISTA FORMULARIO 2
# ##############################################
def formulario2(request, pais, cedis, campania):
    pais_select = pais
    cedi_select = cedis
    campania_select = campania

    context = consulta(pais_select, cedi_select, campania_select)

    return render(request, 'formulario/formulario2.html', context=context)



# ##############################################
# VISTA consulta
# ##############################################
'''
Para evitar repetir código en las vistas formulario y formulario2, 
se crea la función consulta para proveerles el contexto, ya que en 
ambas es el mismo.
'''
def consulta(pais, cedi, campania):

    pais_select = pais
    cedi_select = cedi
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

    return context

